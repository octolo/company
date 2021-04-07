from django import forms
from company import get_company_model, backends_loop, create_company
CompanyModel = get_company_model()

class CompanySearchByCountryForm(forms.Form):
    search = forms.CharField(required=True)

class CompanyAddByCountry(forms.ModelForm):
    position = forms.IntegerField(required=True)
    search = forms.CharField(required=True)
    error_messages = { 'invalid_search': 'test', }

    def __init__(self, country_model, country_fields, parent_object=None, admin=False, *args, **kwargs):
        self.country_model = country_model
        self.country_fields = country_fields
        self.parent_object = parent_object
        super().__init__(*args, **kwargs)

    def get_results(self, country, search):
        message, companies, total, pages = backends_loop(country, search)
        return {
            'search': search,
            'object_list': companies,
            'message': message,
            'total': total,
            'pages': pages,
            'error': False,#cf.message,
        }

    def save(self, commit=True, user=None, author=None):
        results = self.get_results('fr', self.cleaned_data.get('search'))
        data = results['object_list'][self.cleaned_data.get('position')]
        self.new_company = create_company('fr', data)