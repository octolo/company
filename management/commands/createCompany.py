from mighty.management import ModelBaseCommand
from company import  backends_loop, create_company
from mighty.functions import request_kept

class Command(ModelBaseCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--country', default="fr")
        parser.add_argument('--info', default=None)

    def handle(self, *args, **options):
        self.country = options.get('country')
        self.info = options.get('info')
        super(ModelBaseCommand, self).handle(*args, **options)

    def do(self):
        message, companies, total, pages = backends_loop(self.country, self.info)
        if len(companies) > 0:
            request_kept.request.user = self._user
            data, self.new_company = create_company(self.country, companies[0])