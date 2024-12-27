import logging
import random
import re
import time

import requests

from company.choices import fr as choices

logger = logging.getLogger(__name__)


class SearchBackend:
    _logger = logger
    show_by_page = 25
    base_delay = 1.0
    max_delay = 16.0
    delay_with_jitter = 0.5
    retries = 0
    max_retries = 5
    error_count = 0
    max_errors = 5
    raw_address = "%(address)s, %(locality)s %(postal_code)s"
    auto_fields = (
        "show_by_page",
        "base_delay",
        "max_delay",
        "delay_with_jitter",
        "max_retries",
        "max_errors",
    )
    search_types = {}
    fields_association = {}
    data_format = []

    def calculate_delay(self, base_delay, retries, max_delay):
        delay = min(base_delay * (2 ** retries), max_delay)
        jitter = random.uniform(0, 0.1 * delay)
        return delay + jitter

    def retry_with_backoff(self, operation, exceptions=(Exception,), return_on_failure=None):
        retries = 0
        while self.retries < self.max_retries:
            try:
                return operation()
            except exceptions as e:
                self.retries += 1
                if self.retries >= self.max_retries:
                    self._logger.error("Failed after %d retries (exception: %s)", self.retries, e)
                    if return_on_failure is not None:
                        return return_on_failure
                    raise e
                else:
                    delay_with_jitter = self.calculate_delay(self.base_delay, self.retries, self.max_delay)
                    self._logger.info("Operation failed (attempt %d). Retrying in %.2f seconds... (exception: %s)", retries, delay_with_jitter, e)
                    time.sleep(delay_with_jitter)

    def get_search_type(self, search):
        for key, value in self.search_types.items():
            if re.match(value, search):
                return key
        return "text"

    def __init__(self, *args, **kwargs):
        for field in self.auto_fields:
            setattr(self, field, kwargs.get(field, getattr(self, field)))

    def do_request(self, url, method="get", **kwargs):
        self._logger.info(f"GET {url}, Request: {kwargs}")
        response = getattr(requests, method)(url, **kwargs)
        response.raise_for_status()
        return response, response.status_code

    def getattr_recursive(self, obj, strtoget, split=".", default=None):
        keys = strtoget.split(split)
        current = obj
        try:
            for key in keys:
                if isinstance(current, dict):  # Si c'est un dictionnaire
                    current = current[key]
                elif hasattr(current, key):    # Si c'est une classe avec l'attribut
                    current = getattr(current, key)
            return current
        except (KeyError, AttributeError, TypeError):
            pass
        return default

    def get_results(self, search, page=1):
        raise NotImplementedError("You must implement the get_data method")

    def get_value(self, obj, key, name=None, default=None):
        if hasattr(self, "get_value_" + key):
            return getattr(self, "get_value_" + key)(obj)
        if key in self.fields_association and isinstance(self.fields_association[key], tuple):
            for field in self.fields_association[key]:
                value = self.getattr_recursive(obj, field)
                if value:
                    return value
            return default
        return self.getattr_recursive(obj, self.fields_association.get(key, key))

    def get_entities_json(self, data):
        entities = []
        for entity in data:
            data_entity = self.get_data_json(entity)
            entities.append(data_entity)
        return entities

    def get_data_json(self, entity, data_format=None, name=None):
        data = {}
        data_format = data_format or self.data_format
        for field in data_format:
            if isinstance(field, str):
                data[field] = self.get_value(entity, field, name=name)
            elif isinstance(field, dict):
                key = list(field.keys())[0]
                sub = field[key]
                data[key] = self.get_data_json(entity, data_format=sub, name=key)
            elif isinstance(field, list) or isinstance(field, tuple):
                return [self.get_data_json(entity, subfield, name) for subfield in field]
        return data

    def search(self, search, *args, **kwargs):
        total, results = self.retry_with_backoff(lambda: self.get_results(search, *args, **kwargs), return_on_failure=(0, []))
        return total, self.get_entities_json(results)
