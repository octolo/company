import time

from django.db import transaction

from company.backends.insee import CompanyFillerBackend
from mighty.management import ModelBaseCommand


class Command(ModelBaseCommand):
    number = 1000
    offset = 0
    model_company = None
    model_address = None

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--number', default=self.number)
        parser.add_argument('--offset', default=self.offset)
        parser.add_argument('--format', default='csv')
        parser.add_argument('--siret', default=None)
        parser.add_argument('--siren', default=None)

    def handle(self, *args, **options):
        self.number = int(options.get('number', self.number))
        self.offset = int(options.get('offset', self.offset))
        self.format = int(options.get('format', self.offset))
        self.siret = int(options.get('siret', self.offset))
        self.siren = int(options.get('siren', self.offset))
        super(ModelBaseCommand, self).handle(*args, **options)

    def get_queryset(self, *args, **kwargs):
        number = kwargs.get('number', self.number)
        offset = kwargs.get('offset', self.offset)
        time.sleep(1)
        backend = CompanyFillerBackend()
        companies, _total, _pages = backend.get_company_by_siren(
            siren, number, offset
        )
        return companies

    def each_objects(self):
        while True:
            objs = self.get_queryset()
            if objs:
                self.offset += self.number
                with transaction.atomic():
                    for obj in objs:
                        address = obj.pop('address')
                        company, _company_created = (
                            self.model_company.objects.update_or_create(
                                **obj, defaults={'siren': obj['siren']}
                            )
                        )
                        address['company'] = company
                        address, _address_created = (
                            self.model_address.objects.get_or_create(**address)
                        )
            else:
                break
