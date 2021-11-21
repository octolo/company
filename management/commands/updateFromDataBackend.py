from django.db import transaction
from mighty.management import ModelBaseCommand
from company import get_company_model, get_backend_data
import time

class Command(ModelBaseCommand):
    do_on_all = False
    backend_path = None
    manager = "objects"
    backend = None
    list_to_set = [
        "site",
        "ticker",
        "market",
        "icb",
        "capital_division",
        "floating",
        "capitalisation",
        "effective",
        "current",
        "securities",
        "dividend",
        "net_profit",
        "turnover",
    ]

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--backend')
        parser.add_argument('--all', action="store_true")
        parser.add_argument('--siret', default=None)
        parser.add_argument('--isin', default=None)

    def handle(self, *args, **options):
        self.backend_path = options.get('backend')
        self.do_on_all = options.get('all')
        self.siret = options.get('siret')
        self.isin = options.get('isin')
        super(ModelBaseCommand, self).handle(*args, **options)

    @property
    def model_use(self):
        return get_company_model("CompanyFR")

    def do(self):
        if self.backend_path:
            self.logger.info("backend path: %s" % self.backend)
            if self.in_test:
                CompanyModel = self.model_use
                self.current_object = CompanyModel()
                self.current_object.company = get_company_model()()
                self.current_object.denomination = "Test"
                self.current_object.isin = self.isin
                #self.current_object.isin = self.isin
                self.on_object(self.current_object)
            elif self.siret or self.isin:
                self.current_object = self.model_use
                self.on_object(self.current_object)
            elif self.do_on_all:
                self.each_objects()
            else:
                self.logger.warning("--siret, --isin or --all param needed")
        else:
            self.logger.warning("--backend param needed")

    def on_object(self, obj):
        self.logger.info(self.backend)
        self.backend = get_backend_data(self.backend_path)(obj=obj)
        for data in self.list_to_set:
            self.backend.set_one_data(data)
        for data in self.list_to_set:
            try:
                self.logger.debug("%s: %s" % (data, getattr(self.backend.obj.company, data)))
            except Exception:
                self.logger.debug("%s: %s" % (data, getattr(self.backend.obj, data)))
