from mighty.management import CSVModelCommand
from company import backends_loop, create_company
from mighty.functions import request_kept

class Command(CSVModelCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--country', default="fr")
        parser.add_argument('--info', default=None)

    def handle(self, *args, **options):
        self.country = options.get('country')
        self.info = options.get('info')
        super().handle(*args, **options)

    def do(self):
        if self.csvfile:
            self.loop_qs("on_row")
        else:
            self.create_company(self.country, self.info)

    def on_row(self, row):
        self.create_company(row["country"], row["info"])
        if self.position >= 1:
            self.stop_loop = True

    def create_company(self, country, info):
        message, companies, total, pages = backends_loop(country, info)
        if len(companies) > 0:
            data, new_company = create_company(country, companies[0])
