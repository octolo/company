from company.forms.fr import CompanySearchFRForm
from mighty.views.form import FormDescView


class SearchFrFormDescView(FormDescView):
    form = CompanySearchFRForm
