from django.apps import AppConfig
from django.conf import settings


class CompanyConfig(AppConfig):
    name = 'company'
    app_label = getattr(settings, 'COMPANY_APP_LABEL', 'company')
    countries = {
        'fr': getattr(settings, 'COMPANY_APP_LABEL', 'company') + '_companyfr',
        'news': getattr(settings, 'COMPANY_APP_LABEL', 'company') + '_companynews',
    }
    sz_fields = ()
    named_id = True
    named_tpl = '%(named)s-%(id)s'

    class FR:
        list_to_set = [
            'site',
            'ticker',
            'market',
            'icb',
            'capital_division',
            'floating',
            'valorisation',
            'effective',
            'current',
            'securities',
            'dividend',
            'net_profit',
            'turnover',
        ]

    class Model:
        Company = 'Company'
        CompanyFR = 'CompanyFR'
        CompanyAddressFR = 'CompanyAddressFR'
        Balo = 'Balo'

    class Announce:
        Balo = False
        Balo_dateformat = '%Y%m%d'

    def ready(self):
        from . import signals  # noqa
