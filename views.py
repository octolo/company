from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator

from mighty.views import TemplateView, FormView, DetailView, AddView, ListView
from mighty.functions import get_form_model
from mighty.filters import FiltersManager, Foxid

from company.apps import CompanyConfig as conf
from company.models import Company
from company.forms import CompanySearchByCountryForm, CompanyAddByCountry
from company import backends_loop, get_company_model, translates as _, filters, fields
import datetime

company_model = get_company_model()

class CanContainParentObject:
    country = None
    parent_object = None

    def get_country(self):
        return self.kwargs.get('country', self.country)

    def get_country_fields(self):
        return fields.country + getattr(fields, self.get_country())[0:5]

    def get_country_model(self):
        return get_company_model(getattr(conf.Model, 'Company%s' % self.get_country().upper()))

    def get_country_form(self):
        return get_form_model(self.get_country_model(), form_class=CompanyAddByCountry, form_fields=self.get_country_fields())

    def get_parent_object(self):
        if self.parent_object:
            return self.parent_object
        elif self.kwargs.get('uid'):
            return company_model.objects.get(uid=self.kwargs.get('uid') )
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'fake': company_model()})
        parent_object_uid = context.get('object_id', self.kwargs.get('uid'))
        if not context.get('parent_object') and parent_object_uid:
            parent_object = company_model.objects.get(uid=parent_object_uid)
            context.update({'parent_object': parent_object})
        return context

@method_decorator(login_required, name='dispatch')
class ChoiceCountry(CanContainParentObject, TemplateView):
    template_name = "company/country_choice.html"

    def get_countries(self):
        alpha2 = [alpha2 for alpha2, backends in settings.COMPANY_BACKENDS.items()]
        if 'mighty.applications.nationality' in settings.INSTALLED_APPS:
            from mighty.models import Nationality
            nationalities = {nat[0].lower(): {'alpha2': nat[0].lower(), 'image': nat[1]} for nat in Nationality.objects.values_list('alpha2', 'image')}
            return [nationalities[al] if al in nationalities else {'alpha2': al.lower(), 'image': None}  for al in alpha2]
        return [{'alpha2': al.lower(), 'image': None} for al in alpha2]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object_list': self.get_countries()})
        return context

@method_decorator(login_required, name='dispatch')
class SearchByCountry(CanContainParentObject, FormView):
    template_name = "company/country_search.html"
    form_class = CompanySearchByCountryForm
    success_url = '/company/search/'
    over_no_permission = True
    over_add_to_context = {'search': _.search, 'search_placeholder': _.search_placeholder, 'since': _.since}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = self.get_country()
        context.update({
            'fake_country': self.get_country_model()(),
            'country': country,
            'country_fields': self.get_country_fields(),
        })
        if 'mighty.applications.nationality' in settings.INSTALLED_APPS:
            from mighty.models import Nationality
            nationality = Nationality.objects.get(alpha2__iexact=country)
            context.update({'nationality': nationality})
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            message, companies, total, pages = backends_loop(self.kwargs.get('country', 'fr'), search)
            context.update({
                'search': search,
                'object_list': companies,
                'message': message,
                'total': total,
                'pages': pages,
                'error': False,#cf.message,
                'results': _.results % total if int(total) > 1 else _.result % total,
                'strpages': _.pages % pages if int(pages) > 1 else _.page % pages,
                'toomuch': _.toomuch % total,
            })
        return context

@method_decorator(login_required, name='dispatch')
class AddByCountry(CanContainParentObject, FormView):
    template_name = 'company/countries/add.html'
    admin = False

    def get_form_class(self):
        return self.get_country_form()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            "country_model": self.get_country_model(),
            "country_fields": self.get_country_fields(),
            "parent_object": self.get_parent_object(),
            "admin": self.admin,
        })
        return kwargs

    def form_valid(self, form):
        form.save()
        self.success_url = form.cmodel.company.admin_change_url if self.admin else form.cmodel.company.detail_url
        return super().form_valid(form)

if 'rest_framework' in settings.INSTALLED_APPS:
    from rest_framework.generics import ListAPIView, RetrieveAPIView
    from company import serializers, filters

    class APICompanyList(ListAPIView):
        queryset = company_model.objectsB.all()
        serializer_class = serializers.CompanySerializer

        def get_filters(self):
            return [
                filters.SearchByUid(),
                filters.SearchByCompany(),
                filters.SearchByICB(),
                filters.SearchByMarket(),
                #filters.SearchByFloat(),
                filters.SearchFRByAPE(),
                filters.SearchFRByGovernance(),
                filters.SearchFRByEvaluation(),
                filters.SearchFRByISIN(),
                filters.SearchFRByLegalform(),
                filters.SearchFRBySiret(),
                filters.SearchFRByIndex(),
            ]

        def get_filters_manager(self):
            return FiltersManager(flts=self.get_filters())

        def get_queryset(self, queryset=None):
            fm = self.get_filters_manager()
            return Foxid(self.queryset, self.request, f=fm.flts, distinct=True).ready()\
                .filter(*fm.get_filters(self.request, False))\
                .exclude(*fm.get_filters(self.request, True))

    class APICompanyDetail(RetrieveAPIView):
        queryset = company_model.objects.all()
        serializer_class = serializers.CompanySerializer
        lookup_field = 'uid'