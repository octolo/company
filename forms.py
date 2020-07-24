from django import forms

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

    def save(self, commit=True, user=None, author=None):
        model_datas = {field: self.cleaned_data.get(field) for field in self.country_fields}
        if self.parent_object: model_datas.update({"company": self.parent_object})
        self.cmodel, status = self.country_model.objects.get_or_create(**model_datas)
        self.cmodel.save()