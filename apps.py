from django.apps import AppConfig
from django.conf import settings
from mighty import over_config

class Config:
    app_label = 'company'
    countries = {}
    sz_fields = ()
    named_id = True
    named_tpl = "%(named)s-%(id)s"

    class Model:
        Company = 'Company'
        CompanyFR = 'CompanyFR'
        CompanyAddressFR = 'CompanyAddressFR'
        Balo = 'Balo'

    class Announce:
        Balo = False
        Balo_dateformat = '%Y%m%d'

if hasattr(settings, 'COMPANY'): over_config(Config, settings.COMPANY)
class CompanyConfig(AppConfig, Config):
    name = 'company'

    def ready(self):
        from . import signals
