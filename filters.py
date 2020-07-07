
from mighty.filters import Filter
from company.models import Company
from company.fields import searchs, params

def CompanyFilter(request):
    CompanyFilter = Filter(request, Company)
    CompanyFilter.queryset = Company.objectsB
    for search in searchs: CompanyFilter.add_param("search", search)
    for param in params: CompanyFilter.add_param(param, param)
    return CompanyFilter.get()