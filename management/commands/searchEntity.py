from django.core.management.base import BaseCommand

from company.backends import search_entity

# "octolo",
# "917432254",
# "91743225400014",
# "W751042370",


class Command(BaseCommand):
    help = 'Search for companies'

    def add_arguments(self, parser):
        parser.add_argument(
            'country', type=str, help='Country code', default='fr'
        )
        parser.add_argument(
            'search',
            type=str,
            help='Company/Association name or SIREN/SIRET/NRA number',
        )

    def handle(self, *args, **kwargs):
        total, results = search_entity(kwargs['country'], kwargs['search'])

        print()
        for result in results:
            print(result)
            print()

        print(f'Found {total} result(s)')
