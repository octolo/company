from django.test import TestCase
from company.apps import CompanyConfig
from company import create_at_unique, get_company_model

# Create your tests here.
class FRTestCase(TestCase):
    company_cache = None

    @property
    def siren(self):
        return CompanyConfig.Test.fr_siren

    @property
    def company(self):
        if not self.company_cache:
            CompanyModel = get_company_model()
            self.company_cache = CompanyModel.objects.get(company_fr__siren=self.siren)
        return self.company_cache

    def setUp(self):
        print('\n')
        create_at_unique('fr', self.siren)
    
    def test_1_company_exist(self):       
        print('-- Company exist --')
        company = self.company
        print("company: %s" % str(self.company))
        self.assertEqual(self.company.pk > 0, True)

    def test_2_has_address(self):
        print('-- Company nb address --')
        nbr_address = self.company.companyfr_address.count()
        print('Nb address: %s' % str(nbr_address))
        self.assertEqual(nbr_address > 0, True)