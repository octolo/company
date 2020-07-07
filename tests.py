from django.test import TestCase
from company import functions
class BackendTestCase(TestCase):
    def test_search_by_siren(self):
        functions.backends_loop('820807246')

    def test_search_by_fulltext(self):
        functions.backends_loop('easy shares')