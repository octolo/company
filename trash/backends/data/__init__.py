from company import choices
from mighty.applications.logger import EnableLogger
from mighty.errors import BackendError


class CompanyDataBackend(EnableLogger):
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    obj = None
    value_update = 0

    def backend_error(self, msg):
        raise BackendError(msg)

    @property
    def tr(self):
        from company import translates

        return translates

    @property
    def choices(self):
        return choices

    @property
    def siren(self):
        return self.siret[:9] if self.siret else None

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.get('obj')

    def set_one_data(self, data):
        self.logger.info(f'set data: {data}')
        value = getattr(self, f'data_{data}')
        old_value = (
            getattr(self, f'get_data_{data}')()
            if hasattr(self, f'get_data_{data}')
            else getattr(self.obj.company, data)
        )
        self.logger.info(f'value found: {value}')
        if value and old_value != value:
            self.value_update += 1
            self.logger.info(f'set value: {value}')
            getattr(self, f'set_data_{data}')(value) if hasattr(
                self, f'set_data_{data}'
            ) else setattr(self.obj.company, data, value)

    def get_one_data(self, data):
        value = getattr(self, f'data_{data}')
        self.logger.info(f'value found: {value}')
        return value or getattr(self.obj.company, data, value)

    def save(self):
        if self.value_update > 0:
            self.obj.save()
