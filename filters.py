
from mighty.filters import ParamFilter
from company.models import Company

class ByDate(ParamFilter):
    def __init__(self, id='date', *args, **kwargs):
        super().__init__(id, *args, **kwargs)
        self.param = kwargs.get('param', 'date')
        self.mask = kwargs.get('mask', '')
        self.field = kwargs.get('field', 'since')

class ByStartDate(ParamFilter):
    def __init__(self, id='date_start', *args, **kwargs):
        super().__init__(id, *args, **kwargs)
        self.param = kwargs.get('param', 'date_start')
        self.mask = kwargs.get('mask', '__gte')
        self.field = kwargs.get('field', 'since')

class ByEndDate(ParamFilter):
    def __init__(self, id='date_end', *args, **kwargs):
        super().__init__(id, *args, **kwargs)
        self.param = kwargs.get('param', 'date_end')
        self.mask = kwargs.get('mask', '__lte')
        self.field = kwargs.get('field', 'end')

class InDenomination(ParamFilter):
    def __init__(self, id='in_denomination', *args, **kwargs):
        super().__init__(id, *args, **kwargs)
        self.id = id if id else str(uuid.uuid4())
        self.param = kwargs.get('param', 'in_denomination')
        self.mask = kwargs.get('mask', '__icontains')
        self.field = kwargs.get('field', 'denomination')
        self.dependencies+=[ByDate(), ByStartDate(), ByEndDate()]
