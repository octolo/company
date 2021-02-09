from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.http import JsonResponse

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
    country = 'fr'
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

class SearchByCountryBase(CanContainParentObject):
    def get_results(self, search):
        message, companies, total, pages = backends_loop(self.kwargs.get('country', 'fr'), search)
        return {
            'search': search,
            'object_list': companies,
            'message': message,
            'total': total,
            'pages': pages,
            'error': False,#cf.message,
            'results': _.results % total if int(total) > 1 else _.result % total,
            'strpages': _.pages % pages if int(pages) > 1 else _.page % pages,
            'toomuch': _.toomuch % total,
        }

    def country_definition(self):
        country = self.get_country()
        return {
            'fake_country': self.get_country_model()(),
            'country': country,
            'nationality': self.get_nationality(country),
            'country_fields': self.get_country_fields(),
        }

    def get_nationality(self, country):
        if 'mighty.applications.nationality' in settings.INSTALLED_APPS:
            from mighty.models import Nationality
            nationality = Nationality.objects.get(alpha2__iexact=country)
            return nationality
        return country

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = self.get_country()
        context.update(self.country_definition())
        if self.request.GET.get('search'):
            context.update(self.get_results(self.request.GET.get('search')))
        return context

@method_decorator(login_required, name='dispatch')
class SearchByCountry(SearchByCountryBase, FormView):
    template_name = "company/country_search.html"
    form_class = CompanySearchByCountryForm
    success_url = '/company/search/'
    over_no_permission = True
    over_add_to_context = {'search': _.search, 'search_placeholder': _.search_placeholder, 'since': _.since}

@method_decorator(login_required, name='dispatch')
class APISearchByCountry(SearchByCountryBase, TemplateView):
    def get_context_data(self, **kwargs):
        if self.request.GET.get('search'):
            return self.get_results(self.request.GET.get('search'))
        return {}

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=True, **response_kwargs)

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


from company import create_company
@method_decorator(login_required, name='dispatch')
class AddBySiren(APISearchByCountry):
    def get_context_data(self, **kwargs):
        if self.request.GET.get('siren'):
            results = self.get_results(self.request.GET.get('siren'))
            if len(results['object_list']) == 1:
                create_company('FR', results['object_list'][0])
                return results['object_list'][0]
        return {}

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=True, **response_kwargs)

from mighty.views import CheckData
class CompanyCheck(CheckData):
    model = company_model
    test_field = 'company_fr__siren'
    

#@method_decorator(login_required, name='dispatch')
#class DetailBySiren(DetailView):
#    model = company_model
#
#    def get_object(self):
#        self.model.objects.get(company_fr__siren=self.request)

if 'rest_framework' in settings.INSTALLED_APPS:
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework.generics import ListAPIView, RetrieveAPIView
    from company import serializers, filters
    from mighty.filters import FiltersManager, Foxid

    class APICompanyList(ListAPIView):
        queryset = company_model.objectsB.all()
        serializer_class = serializers.CompanySerializer
        lookup_field = 'uid'
        filters = filters.filters_list
        cache_manager = None

        @property
        def foxid(self):
            return Foxid(self.queryset, self.request, f=self.manager.flts).ready()

        @property
        def manager(self):
            if not self.cache_manager:
                self.cache_manager = FiltersManager(flts=self.filters)
            return self.cache_manager

        def get_queryset(self, queryset=None):
            return self.foxid.filter(*self.manager.params(self.request))

    class APICompanyDetail(RetrieveAPIView):
        queryset = company_model.objects.all()
        serializer_class = serializers.CompanySerializer
        lookup_field = 'uid'

    class APISearchByCountry(SearchByCountryBase, APIView):
        def get_context_data(self, **kwargs):
            if self.request.GET.get('search'):
                return self.get_results(self.request.GET.get('search'))
            return {}

        def get(self, request, format=None):
            return Response(self.get_context_data())

    class AddBySiren(SearchByCountryBase, APIView):
        def get_context_data(self, **kwargs):
            if self.request.GET.get('siren'):
                results = self.get_results(self.request.GET.get('siren'))
                if len(results['object_list']) == 1:
                    create_company('FR', results['object_list'][0])
                    return results['object_list'][0]
            return {}

        def get(self, request, format=None):
            return Response(self.get_context_data())
            