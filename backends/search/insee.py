import base64
import datetime
import logging
import random
import re
import time

import requests
from django.conf import settings

from company.backends.search import SearchBackend
from mighty.functions import make_searchable

logger = logging.getLogger(__name__)


class SearchBackend(SearchBackend):
    token_url = 'https://api.insee.fr/token'
    # siren_url = 'https://api.insee.fr/entreprises/sirene/V3/siren'
    # siret_url = 'https://api.insee.fr/entreprises/sirene/V3/siret'
    siren_url = 'https://api.insee.fr/api-sirene/3.11/siren'
    siret_url = 'https://api.insee.fr/api-sirene/3.11/siret'
    since_format = '%Y-%m-%d'
    iso_format = '%Y-%m-%dT%H:%M:%S'
    error = 5
    raw_address = "%(address)s, %(locality)s %(postal_code)s"

    def __init__(self, max_retries=5, base_delay=1, max_delay=32):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay

    def call_webservice(self, url, headers, postfields=None):
        """Makes a web service call with exponential backoff."""
        retries = 0

        while retries < self.max_retries:
            try:
                if postfields:
                    response = requests.post(url, headers=headers, data=postfields)
                else:
                    response = requests.get(url, headers=headers)

                # Log response status and return JSON data
                logger.info("URL: %s, Status Code: %d", url, response.status_code)
                response.raise_for_status()  # Raise HTTPError for bad responses
                return response.json(), response.status_code

            except requests.exceptions.RequestException as e:
                # Log specific errors
                logger.warning("Error: %s", e)

                # Exponential backoff with jitter
                retries += 1
                if retries >= self.max_retries:
                    logger.error("Max retries reached. Giving up.")
                    raise e

                delay = min(self.base_delay * (2 ** retries), self.max_delay)
                delay_with_jitter = delay + random.uniform(0, 0.1 * delay)
                logger.info("Retrying in %.2f seconds...", delay_with_jitter)
                time.sleep(delay_with_jitter)

        # If all retries are exhausted, raise an exception
        raise RuntimeError("Failed to complete the web service call after retries.")

    def get_token(self):
        basic = '%s:%s' % (settings.INSEE_KEY, settings.INSEE_SECRET)
        basic = base64.b64encode(basic.encode('utf-8')).decode('utf-8')
        headers = {
            "accept": "application/json",
            "Authorization": "Basic %s" % basic,
        }
        postfields = {"grant_type": "client_credentials"}

        try:
            data, status = self.call_webservice(self.token_url, headers, postfields)
            logger.info("Response Data: %s", data, status)
            return data["access_token"]
        except Exception as e:
            logger.error("Failed to call webservice: %s", e)

    def get_companies(self, qreq, number=50, offset=0):
        message, companies, total, pages = (False, [], 0, 0)
        # access_token = self.get_token()
        # headers = {'Accept': 'application/json', 'Authorization': 'Bearer %s' % access_token}
        headers = {'Accept': 'application/json', "X-INSEE-Api-Key-Integration": settings.INSEE_API_KEY}
        url = "%s?q=%s&nombre=%s&debut=%s&masquerValeursNulles=true" % (self.siret_url, qreq, number, offset)
        buffer, response_code = self.call_webservice(url, headers)
        if 'header' in buffer:
            message = False if buffer['header']['message'] == "OK" else buffer['header']['message']
            total = buffer['header'].get('total', 0)
            pages = round(total / number) if total else 0
            if str(response_code)[0] in ["2", "3"]:
                for company in buffer.get('etablissements', [buffer['header']]):
                    logger.debug(company)
                    new_company = {
                        'siret': company.get('siret'),
                        'denomination': company['uniteLegale'].get('denominationUniteLegale', company['uniteLegale'].get('nomUniteLegale')),
                        'legalform': company['uniteLegale']['categorieJuridiqueUniteLegale'],
                        'ape': company['uniteLegale']['activitePrincipaleUniteLegale'].replace('.', ''),
                        'ape_noun': company['uniteLegale']['nomenclatureActivitePrincipaleUniteLegale'],
                        'since': self.since(company['uniteLegale'].get('dateCreationUniteLegale')),
                        'category': company['uniteLegale'].get('categorieEntreprise', ''),
                        'slice_effective': company['uniteLegale'].get('trancheEffectifsUniteLegale', ''),
                        'siege': company.get('etablissementSiege', False),
                        'rna': company['uniteLegale'].get('identifiantAssociationUniteLegale', None),
                        'address': {
                            'address': ' '.join(filter(None, [
                                company['adresseEtablissement'].get('numeroVoieEtablissement'),
                                company['adresseEtablissement'].get('typeVoieEtablissement'),
                                company['adresseEtablissement'].get('libelleVoieEtablissement')
                            ])),
                            'complement': company['adresseEtablissement'].get('complementAdresseEtablissement', ''),
                            'locality': company['adresseEtablissement'].get('libelleCommuneEtablissement',
                                                                            company['adresseEtablissement'].get('libelleCommuneEtrangerEtablissement', '')),
                            'postal_code': company['adresseEtablissement'].get('codePostalEtablissement',
                                                                               company['adresseEtablissement'].get('codeCommuneEtablissement', '')),
                            'country': company['adresseEtablissement'].get('libellePaysEtrangerEtablissement', 'france').lower(),
                            'country_code': company['adresseEtablissement'].get('codePaysEtrangerEtablissement', 'fr').lower(),
                            'cedex': company['adresseEtablissement'].get('libelleCedexEtablissement', ''),
                            'cedex_code': company['adresseEtablissement'].get('codeCedexEtablissement', ''),
                            'special': company['adresseEtablissement'].get('distributionSpecialeEtablissement', ''),
                            'index': company['adresseEtablissement'].get('indiceRepetitionEtablissement', ''),
                            'nic': company.get('nic')
                        }
                    }
                    new_company['raw_address'] = self.raw_address % (new_company['address'])
                    new_company['ape_str'] = self.get_ape_str(new_company['ape'])
                    new_company['legalform_str'] = self.get_legalform_str(new_company['legalform'])
                    new_company['slice_str'] = self.get_slice_str(new_company['slice_effective'])
                    companies.append(new_company)
            return message, companies, total, pages
        else:
            if 'fault' in buffer:
                if buffer['fault']['code'] == 900804:
                    sleepfor = 61 - datetime.datetime.now().second
                    i = 0
                    while i < sleepfor:
                        logger.info("desc: %s, wait: %s seconds" % (buffer['fault']['description'], sleepfor))
                        time.sleep(1)
                        sleepfor -= 1
                    return self.get_companies(qreq, number, offset)
                else:
                    logger.info(buffer)
            else:
                logger.info("Error encountered but we dont know what")

    def get_company_by_siren(self, siren):
        return self.get_companies('siren:%s+AND+etablissementSiege:true' % siren)

    def get_company_by_rna(self, rna):
        return self.get_companies('identifiantAssociationUniteLegale:%s+AND+etablissementSiege:true' % rna)

    def get_active_companies(self, number, offset):
        return self.get_companies('etatAdministratifUniteLegale:A', number, offset)

    def get_company_by_fulltext(self, fulltext):
        if len(fulltext) == 10 and fulltext[0] == 'W':
            return self.get_company_by_rna(fulltext)
        fulltext = re.sub(r"\s+", '-', fulltext)
        return self.get_companies('denominationUniteLegale:%s+AND+etatAdministratifUniteLegale:A' % make_searchable(fulltext))
