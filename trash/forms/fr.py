from django import forms


class CompanySearchFRForm(forms.Form):
    search = forms.CharField(required=True, label='Recherche')
