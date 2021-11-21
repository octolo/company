from mighty.functions import similar_text
from mighty.applications.logger import EnableLogger

from company import choices
from io import BytesIO
import re

class CompanyDataBackend(EnableLogger):
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    obj = None

    @property
    def tr(self): 
        from company import translates
        return translates
    @property
    def choices(self): return choices
    @property
    def siren(self): return self.siret[:9] if self.siret else None

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.get("obj")

    def set_one_data(self, data):
        self.logger.info("set data: %s" % data)
        value = getattr(self, "data_%s" % data)
        old_value = getattr(self, "get_data_%s" % data)() if hasattr(self, "get_data_%s" % data) else getattr(self.obj.company, data)
        if old_value != value:
            self.logger.info("set value: %s" % value)
            getattr(self, "set_data_%s" % data)(value) if hasattr(self, "set_data_%s" % data) else setattr(self.obj.company, data, value)

