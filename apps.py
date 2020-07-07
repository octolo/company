from django.apps import AppConfig
from django.conf import settings
from mighty import over_config

class Config:
    class ForeignKey:
        Company = 'Company'

    class Announce:
        Balo = False
        Balo_dateformat = '%Y%m%d'

if hasattr(settings, 'COMPANY'): over_config(Config, settings.COMPANY)
class CompanyConfig(AppConfig, Config):
    name = 'company'
