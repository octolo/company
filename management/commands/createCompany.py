from company import create_entity
from company.backends import search_entity
from mighty.management import CSVModelCommand


class Command(CSVModelCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--country', default='fr')
        parser.add_argument('--info', default=None)

    def handle(self, *args, **options):
        self.country = options.get('country')
        self.info = options.get('info')
        super().handle(*args, **options)

    def do(self):
        if self.csvfile:
            self.loop_qs('on_row')
        else:
            self.create_company(self.country, self.info)

    def on_row(self, row):
        self.create_company(row['country'], row['info'], row)
        if self.position >= 1:
            self.stop_loop = True

    def create_company(self, country, info, row=None):
        total, results = search_entity(country, info)
        if len(results) > 0:
            data, new_company = create_entity(country, results[0])
            if row:
                for k, v in row.items():
                    if k not in ('country', 'info'):
                        if v and hasattr(new_company, k):
                            setattr(new_company, k, v)
                new_company.save()
