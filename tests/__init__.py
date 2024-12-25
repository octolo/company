from django.test import TestCase
from company.backends import search_company_or_association

# Create your tests here.
class TestSearchBackend(TestCase):
    def test_search_fulltext(self):
        results = search_company_or_association("Octolo")
        print(results)
        self.assertTrue(results)

    def test_search_siren(self):
        results = search_company_or_association("917432254")
        print(results)
        self.assertTrue(results)

    def test_search_siret(self):
        results = search_company_or_association("91743225400014")
        print(results)
        self.assertTrue(results)

    def test_search_nra(self):
        results = search_company_or_association("W751042370")
        print(results)
        self.assertTrue(results)
