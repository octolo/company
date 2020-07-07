from django import forms

class CompanySearchForm(forms.Form):
    search = forms.CharField(required=True)