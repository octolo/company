from django.core.management.base import BaseCommand
from company.backends import search_company_or_association

class Command(BaseCommand):
    help = 'Search for companies'

    def add_arguments(self, parser):
        parser.add_argument('search', type=str, help='Company/Association name or SIREN/SIRET/NRA number')

    def handle(self, *args, **kwargs):
        # "octolo",
        # "917432254",
        # "91743225400014",
        # "W751042370",
        search = kwargs['search']
        results = search_company_or_association(search)
        print(results)
