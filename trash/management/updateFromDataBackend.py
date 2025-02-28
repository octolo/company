from company import get_backend_data, get_company_model
from company.apps import CompanyConfig
from company.backends.data import BackendError
from mighty.management import ModelBaseCommand


class Command(ModelBaseCommand):
    do_on_all = False
    backend_path = None
    manager = 'objects'
    backend = None
    list_to_set = CompanyConfig.FR.list_to_set

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--backend')
        parser.add_argument('--all', action='store_true')
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
        if self.siret:
            return get_company_model('CompanyFR').get(siret=self.siret)
        return get_company_model('CompanyFR').get(isin=self.isin)

    def do(self):
        if self.backend_path:
            self.logger.info(f'backend path: {self.backend_path}')
            if self.in_test:
                CompanyModel = self.model_use
                self.current_object = CompanyModel()
                self.current_object.company = get_company_model()()
                self.current_object.denomination = 'Test'
                self.current_object.isin = self.isin
                self.on_object(self.current_object)
            elif self.siret or self.isin:
                self.current_object = self.model_use
                self.on_object(self.current_object)
            elif self.do_on_all:
                self.each_objects()
            else:
                self.logger.warning('--siret, --isin or --all param needed')
        else:
            self.logger.warning('--backend param needed')

    def on_object(self, obj):
        try:
            self.logger.info(self.backend)
            self.backend = get_backend_data(self.backend_path)(obj=obj)
            for data in self.list_to_set:
                self.backend.set_one_data(data)
            self.backend.save()
            for data in self.list_to_set:
                try:
                    self.logger.debug(
                        f'{data}: {getattr(self.backend.obj.company, data)}'
                    )
                except Exception:
                    self.logger.debug(
                        f'{data}: {getattr(self.backend.obj, data)}'
                    )
            # time.sleep(5)
        except BackendError as e:
            self.logger.warning(str(e))
