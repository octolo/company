from mighty.views.form import FormDescView
from company.forms.fr import CompanySearchFRForm

class SearchFrFormDescView(FormDescView):
    form = CompanySearchFRForm
