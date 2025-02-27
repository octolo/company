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
        self.logger.info('set data: %s' % data)
        value = getattr(self, 'data_%s' % data)
        old_value = (
            getattr(self, 'get_data_%s' % data)()
            if hasattr(self, 'get_data_%s' % data)
            else getattr(self.obj.company, data)
        )
        self.logger.info('value found: %s' % value)
        if value and old_value != value:
            self.value_update += 1
            self.logger.info('set value: %s' % value)
            getattr(self, 'set_data_%s' % data)(value) if hasattr(
                self, 'set_data_%s' % data
            ) else setattr(self.obj.company, data, value)

    def get_one_data(self, data):
        value = getattr(self, 'data_%s' % data)
        self.logger.info('value found: %s' % value)
        return value or getattr(self.obj.company, data, value)

    def save(self):
        if self.value_update > 0:
            self.obj.save()
