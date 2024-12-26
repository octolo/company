from django.test import TestCase
from company.backends import search_entity

# Create your tests here.
class TestSearchFrBackend(TestCase):
    def test_search_fulltext(self):
        results = search_entity("fr", "Octolo")
        print(results)
        self.assertTrue(results)

    def test_search_siren(self):
        results = search_entity("fr", "917432254")
        print(results)
        self.assertTrue(results)

    def test_search_siret(self):
        results = search_entity("fr", "91743225400014")
        print(results)
        self.assertTrue(results)

    def test_search_nra(self):
        results = search_entity("fr", "W751042370")
        print(results)
        self.assertTrue(results)
