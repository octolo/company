from django.apps import AppConfig
from django.conf import settings


class CompanyConfig(AppConfig):
    name = 'company'
    app_label = getattr(settings, 'COMPANY_APP_LABEL', 'company')
    countries = {
        'fr': getattr(settings, 'COMPANY_APP_LABEL', 'company') + '_companyfr',
        'news': getattr(settings, 'COMPANY_APP_LABEL', 'company')
        + '_companynews',
    }
    sz_fields = ()
    named_id = True
    named_tpl = '%(named)s-%(id)s'
    document_header_tpl = getattr(settings, 'COMPANY_DOCUMENT_HEADER_TEMPLATE', 'company/templates/document_header.html')
    document_footer_tpl = getattr(settings, 'COMPANY_DOCUMENT_FOOTER_TEMPLATE', 'company/templates/document_footer.html')
    company_class_herit = []
    company_table = getattr(settings, 'COMPANY_TABLE', 'company_company')
    companyaddressfr_table = getattr(settings, 'COMPANYADDRESSFR_TABLE', 'company_companyaddressfr')
    companyfr_table = getattr(settings, 'COMPANYFR_TABLE', 'company_companyfr')
    companystatusconfig_table = getattr(settings, 'COMPANYSTATUSCONFIG_TABLE', 'company_companystatusconfig')
    companystatus_table = getattr(settings, 'COMPANYSTATUS_TABLE', 'company_companystatus')
    fields_to_add = getattr(settings, 'COMPANY_FIELDS_TO_ADD', {})

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

    def model_string(self, model):
        return f'{self.app_label}.{model}'