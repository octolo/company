from django.conf import settings
from mighty.views import CheckData
from company import get_company_model

class CompanyCheckSiren(CheckData):
    model = get_company_model()
    test_field = 'company_fr__siren'
    
class CompanyCheckRna(CheckData):
    model = get_company_model()
    test_field = 'company_fr__rna'
