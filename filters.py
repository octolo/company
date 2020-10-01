from django.db.models import Q
from mighty import filters
from functools import reduce
from company import choices
from company.choices import fr as choices_fr

class SearchByUid(filters.ParamFilter):
    def __init__(self, id='uid', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'uid')
        self.field = kwargs.get('field', 'uid')

class SearchByCompany(filters.SearchFilter):
    def __init__(self, id='search', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'search')
        self.field = {'company': 'search', 'company_fr': 'company_fr__search'}

    def get_Q(self):
        company = reduce(self.operator, [Q(**{self.field['company']+self.mask: value }) for value in self.get_value(self.field['company'])])
        company_fr = reduce(self.operator, [Q(**{self.field['company_fr']+self.mask: value }) for value in self.get_value(self.field['company_fr'])])
        return company|company_fr

class SearchByICB(filters.ParamChoicesFilter):
    def __init__(self, id='icb', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)  
        self.param = kwargs.get('param', 'icb')
        self.field = kwargs.get('field', 'icb')
        self.choices = kwargs.get('choices', [i[0] for i in choices.ICB])

class SearchByMarket(filters.ParamChoicesFilter):
    def __init__(self, id='market', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'market')
        self.field = kwargs.get('field', 'market')
        self.choices = kwargs.get('choices', [m[0] for m in choices.MARKET])

# FR
class SearchFRByISIN(filters.SearchFilter):
    def __init__(self, id='isin', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'isin')
        self.field = kwargs.get('field', 'company_fr__isin')

class SearchFRBySiret(filters.SearchFilter):
    def __init__(self, id='siret', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'siret')
        self.field = kwargs.get('siret', 'company_fr__siret')

class SearchFRByAPE(filters.ParamChoicesFilter):
    def __init__(self, id='ape', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'ape')
        self.field = kwargs.get('field', 'company_fr__ape')
        self.choices = kwargs.get('choices', [a[0] for a in choices_fr.APE])

class SearchFRByLegalform(filters.ParamChoicesFilter):
    def __init__(self, id='legalform', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'legalform')
        self.field = kwargs.get('field', 'legalform')
        self.choices = kwargs.get('choices', [l[0] for l in choices_fr.LEGALFORM])

class SearchFRByGovernance(filters.ParamChoicesFilter):
    def __init__(self, id='governance', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'governance')
        self.field = kwargs.get('field', 'governance')
        self.choices = kwargs.get('choices', [g[0] for g in choices_fr.GOVERNANCE])

class SearchFRByEvaluation(filters.ParamChoicesFilter):
    def __init__(self, id='evaluation', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'evaluation')
        self.field = kwargs.get('field', 'evaluation')
        self.choices = kwargs.get('choices', [e[0] for e in choices_fr.EVALUATION])

class SearchFRByIndex(filters.ParamMultiChoicesFilter):
    def __init__(self, id='index', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.param = kwargs.get('param', 'index')
        self.field = kwargs.get('field', 'company_fr__index')
        self.choices = kwargs.get('choices', [e[0] for e in choices_fr.INDEX])
