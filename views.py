from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from mighty.views import FormView, DetailView, AddView, ListView
from mighty.views.viewsets import ModelViewSet
from company.apps import CompanyConfig as conf
from company.models import Company
from company.forms import CompanySearchForm
from company import translates as _, filters
from company import backends_loop
import datetime

@method_decorator(login_required, name='dispatch')
class SearchByCountry(FormView):
    template_name = "company/list.html"
    form_class = CompanySearchForm
    success_url = '/company/search/'
    over_no_permission = True
    over_add_to_context = {
        'legalform': _.legalform,
        'corebusiness': _.corebusiness,
        'search': _.search,
        'search_placeholder': _.search_placeholder,
        'since': _.since
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            message, companies, total, pages = backends_loop(self.kwargs.get('country', 'fr'), search)
            context.update({
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

class DetailByCountry(DetailView):
    template_name = 'company/detail.html'
    model = Company
    slug_field = 'siren'
    slug_url_kwarg = 'siren'
    filler = False
    message = None

    def get_object(self):
        try:
            return Company.objects.get(siren=self.kwargs['siren'])
        except Company.DoesNotExist:
            message, companies, total, pages = backends_loop(self.kwargs.get('country', 'fr'), search)
            self.message = cf.message
            self.filler = True
            return companies[0]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'filler': self.filler, 'error': self.message,})
        if not self.message:
            if self.filler:
                context.update({'title': context['object']['denomination'],})
            else:
                #roles_available = Role.objects.all()
                #roles = Roles.objectsB.filter(tenant=context['object'])
                context.update({
                    'title': context['object'].denomination,
                    #'can_access': roles.filter(user=self.request.user).count() > 0,
                    #'roles': roles,
                    #'roles_available': roles_available
                })
        return context

class List(ListView):
    model = Company
    over_add_to_context = {
        'form': CompanySearchForm,
        'legalform': _.legalform,
        'corebusiness': _.corebusiness,
        'search': _.search,
        'search_placeholder': _.search_placeholder,
        'since': _.since
    }
    
    def get_queryset(self):
        return filters.CompanyFilter(self.request) if self.request.GET.get('search') else Company.objects.none()

class Add(AddView):
    over_fields = ('ape', 'legalform',)
    apiobject = None
    message = None
    date_format = None

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        cf = CompanyFiller()
        companies, total, pages = cf.get_company_by_siren(self.kwargs['siren'])
        self.message = cf.message
        self.filler = True
        self.date_format = cf.date_format
        self.apiobject = companies[0]
        if self.apiobject['ape_code']:
            form.fields['ape'].initial = self.apiobject['ape_code']
        if self.apiobject['legalform_code']:
            form.fields['legalform'].initial = int(self.apiobject['legalform_code'])
        return form

    def form_valid(self, form):
        form.instance.siren = self.apiobject['siren']
        form.instance.denomination = self.apiobject['denomination']
        form.instance.ape = self.apiobject['ape_code']
        form.instance.since = datetime.datetime.strptime(self.apiobject['since'], self.date_format).date()
        return super().form_valid(form)

    def get_success_url(self):
        role, role_created = Role.objects.get_or_create(name='manager')
        tenant, tenant_created = Tenant.objects.get_or_create(tenant=self.object, user=self.request.user)
        tenant.roles.add(role)
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.message: context.update({'object': self.apiobject,})
        return context

class CompanyViewSet(ModelViewSet):
    model = Company
    slug = '<str:siren>'
    filter_model = filters.CompanyFilter

    def __init__(self):
        super().__init__()
        self.add_view('detail', Detail, 'detail/%s/' % self.slug)
        self.add_view('add', Add, 'add/%s/' % self.slug)
        self.add_view('search', Search, 'search/')
        self.add_view('list', List, '')