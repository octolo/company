from django.db.models import Q
from mighty import filters
from functools import reduce
from company import choices
from company.choices import fr as choices_fr

class SearchByUid(filters.ParamFilter):
    def __init__(self, id='uid', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.field = kwargs.get('field', 'uid')

class SearchFilter(filters.SearchFilter):
    def __init__(self, id='search', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

    def get_field(self):
        return {'company': self.prefix + 'search' + self.mask, 'company_fr': self.prefix + 'company_fr__search'+ self.mask}

    def get_Q(self):
        company = reduce(self.operator, [Q(**{self.get_field()['company']: value }) for value in self.get_value()])
        company_fr = reduce(self.operator, [Q(**{self.get_field()['company_fr']: value }) for value in self.get_value()])
        return company|company_fr

class SearchByICB(filters.ParamMultiChoicesFilter):
    def __init__(self, id='icb', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.choices_required = True
        self.choices = kwargs.get('choices', [i[0] for i in choices.ICB])
        #self.field = kwargs.get('field', 'icb')

class SearchByMarket(filters.ParamMultiChoicesFilter):
    def __init__(self, id='market', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.choices = kwargs.get('choices', [m[0] for m in choices.MARKET])

class IsDowjones(filters.BooleanParamFilter):
    def __init__(self, id='dowjones', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

class IsNasdaq(filters.BooleanParamFilter):
    def __init__(self, id='nasdaq', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

class IsGaia(filters.BooleanParamFilter):
    def __init__(self, id='gaia', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

class SearchByEffective(filters.FilterByGTEorLTE):
    def __init__(self, id='effective', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.is_int = True

class SearchByFloating(filters.FilterByGTEorLTE):
    def __init__(self, id='floating', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

class SearchByTurnover(filters.FilterByGTEorLTE):
    def __init__(self, id='turnover', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

class HasSettleTnternal(filters.BooleanParamFilter):
    def __init__(self, id='settle_internal', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

class DurationMandate(filters.FilterByGTEorLTE):
    def __init__(self, id='duration_status', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.is_int = True
        self.field = kwargs.get('field', 'duration_mandate')

class HasAgeLimitPDG(filters.BooleanParamFilter):
    def __init__(self, id='age_limit_pdg', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

class HasAgeLimitDG(filters.BooleanParamFilter):
    def __init__(self, id='age_limit_dg', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

class HasStockMinRule(filters.FilterByGTEorLTE):
    def __init__(self, id='stock_min_rule', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.is_int = True

    #def format_value(self, value):
    #    return False if value else True

class HasStockMinStatus(filters.FilterByGTEorLTE):
    def __init__(self, id='stock_min_status', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.is_int = True
        

    #def format_value(self, value):
    #    return False if value else True

class HasMatrixSkills(filters.BooleanParamFilter):
    def __init__(self, id='matrix_skills', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)

# FR
class SearchByCoderef(filters.ParamMultiChoicesFilter):
    def __init__(self, id='coderef', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.field = kwargs.get('field', 'company_fr__coderef')
        self.choices = kwargs.get('choices', [m[0] for m in choices_fr.CODEREF])

class SearchFRByISIN(filters.SearchFilter):
    def __init__(self, id='isin', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.field = kwargs.get('field', 'company_fr__isin')

class SearchFRBySiret(filters.SearchFilter):
    def __init__(self, id='siret', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.field = kwargs.get('siret', 'company_fr__siret')

class SearchFRByAPE(filters.ParamMultiChoicesFilter):
    def __init__(self, id='ape', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.field = kwargs.get('field', 'company_fr__ape')
        self.choices = kwargs.get('choices', [a[0] for a in choices_fr.APE])

class SearchFRByLegalform(filters.ParamMultiChoicesFilter):
    def __init__(self, id='legalform', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.field = kwargs.get('field', 'company_fr__legalform')
        self.choices = kwargs.get('choices', [l[0] for l in choices_fr.LEGALFORM])

class SearchFRByGovernance(filters.ParamMultiChoicesFilter):
    def __init__(self, id='governance', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.choices_required = False
        self.field = kwargs.get('field', 'company_fr__governance')
        self.choices = kwargs.get('choices', [g[0] for g in choices_fr.GOVERNANCE])

class SearchFRByEvaluation(filters.ParamMultiChoicesFilter):
    def __init__(self, id='evaluation', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.choices_required = True
        self.field = kwargs.get('field', 'company_fr__evaluation')
        self.choices = kwargs.get('choices', [e[0] for e in choices_fr.EVALUATION])

class SearchFRByIndex(filters.ParamMultiChoicesFilter):
    def __init__(self, id='index', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.choices_required = True
        self.field = kwargs.get('field', 'company_fr__index')
        self.choices = kwargs.get('choices', [e[0] for e in choices_fr.INDEX])

class SearchFRBySliceEffective(filters.ParamMultiChoicesFilter):
    def __init__(self, id='slice', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.choices_required = True
        self.field = kwargs.get('field', 'company_fr__slice_effective')
        self.choices = kwargs.get('choices', [e[0] for e in choices_fr.SLICE_EFFECTIVE])

class SearchByNews(filters.SearchFilter):
    def __init__(self, id='news', request=None, *args, **kwargs):
        super().__init__(id, request, *args, **kwargs)
        self.field = kwargs.get('field', 'company_news__keywords')

filters_list = [
    SearchFilter(),
    SearchByUid(),

    # Actualités
    SearchByNews(),

    #Index/ICB/Market
    SearchFRByIndex(),
    SearchByICB(),
    SearchByMarket(),
    IsDowjones(),
    IsNasdaq(),
    IsGaia(),

    # Flottants/Chiffre
    SearchByFloating(),
    SearchByTurnover(),
    SearchByCoderef(),
    
    # Effectif/Durée de mandat/matrice de compétences
    SearchByEffective(),
    DurationMandate(),
    HasMatrixSkills(),

    # Limite d'age PDG/DG
    HasAgeLimitPDG(),
    HasAgeLimitDG(),

    # Stock reglement/status
    HasSettleTnternal(),
    HasStockMinRule(),
    HasStockMinStatus(),

    # FR - API/Governance/Evaluation/ISIN/LegalForm/Siret/Effectif
    SearchFRByAPE(),
    SearchFRByGovernance(),
    SearchFRByEvaluation(),
    SearchFRByISIN(),
    SearchFRByLegalform(),
    SearchFRBySiret(),
    SearchFRBySliceEffective(),
]