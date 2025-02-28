from django.contrib import admin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import path
from django.utils.module_loading import import_string

from company import create_entity, fields, get_company_model
from company.apps import CompanyConfig as conf
from company.backends import search_entity
from company.choices.countries import get_country_by
from mighty.admin.models import BaseAdmin
from mighty.applications.address import fields as address_fields
from mighty.applications.address.admin import AddressAdminInline

CompanyModel = get_company_model('Company')


class CompanyAdmin(BaseAdmin):
    fieldsets = (
        (None, {'classes': ('wide',), 'fields': (
            'denomination',
            'image',
            'since',
            'site',
            'effective',
            'secretary',
            'resume',
        )}),
    )
    list_display = ('denomination', 'since', 'siege_fr', 'is_type')
    search_fields = ('denomination', 'company_fr__siret')
    readonly_fields = ('siege_fr', 'siege_fr_address')
    search_template = None

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.add_field('Form', fields.form)
        self.add_field('Comex & Purpose', fields.comex_purpose)
        self.add_field('Market', fields.market)
        self.add_field('Rules', fields.rules)
        self.add_field('FR', fields.countryfr)
        if conf.named_id:
            self.add_field('Informations', ('named_id',))
            self.readonly_fields += ('named_id',)

    action_admin_path = 'actions/'
    action_admin_suffix = 'actions'
    action_admin_template = 'admin/company/actions.html'
    action_object_tools = {'name': 'Actions', 'url': 'actions', 'list': True}

    def action_view(self, request, *args, **kwargs):
        return self.admincustom_view(request, urlname=self.get_admin_urlname(self.action_admin_suffix), template=self.action_admin_template)

    country_admin_path = 'actions/<str:action>/countries/'
    country_admin_suffix = 'countries'
    country_admin_template = 'admin/company/countries.html'
    country_object_tools = {'name': 'Countries', 'url': 'countries'}

    def country_view(self, request, action, object_id=None, form_url=None, extra_context=None):
        extra_context = extra_context or {}
        extra_context['action'] = action
        countries = import_string(f'company.backends.{action}_backends')
        extra_context['countries'] = {key: get_country_by(key, 'alpha2') for key in countries}
        return self.admincustom_view(request, object_id, extra_context, urlname=self.get_admin_urlname(self.country_admin_suffix), template=self.country_admin_template)

    search_admin_path = 'actions/search/countries/<str:country>/'
    search_admin_suffix = 'search'
    search_admin_template = 'admin/company/search.html'
    search_object_tools = {'name': 'Search', 'url': 'search'}

    def search_view(self, request, country, object_id=None, form_url=None, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            'country': country,
            'search': request.GET.get('q'),
            'results': [],
            'total': 0
        })
        extra_context['country'] = country
        extra_context['search'] = request.GET.get('q')
        if extra_context['search']:
            total, results = search_entity(country, extra_context['search'])
            extra_context['results'] = results
            extra_context['total'] = total
        return self.admincustom_view(request, object_id, extra_context, urlname=self.get_admin_urlname(self.search_admin_suffix), template=self.search_admin_template)

    create_admin_path = 'actions/create/countries/<str:country>/<str:rna_or_siren>/'
    create_admin_suffix = 'create'
    create_admin_template = 'admin/company/create.html'

    def create_view(self, request, country, rna_or_siren, object_id=None, form_url=None, extra_context=None):
        extra_context = extra_context or {}
        total, results = search_entity(country, rna_or_siren)
        extra_context.update({
            'country': country,
            'rna_or_siren': rna_or_siren,
            'object': results[0],
            'total': total,
        })
        if request.method == 'POST' and request.POST.get('rna_or_siren') == rna_or_siren:
            _info, model = create_entity(country, results[0])
            return redirect(f'admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change', object_id=model.id)
        return self.admincustom_view(request, object_id, extra_context, urlname=self.get_admin_urlname(self.create_admin_suffix), template=self.create_admin_template)

    getorcreate_admin_path = 'actions/getorcreate/countries/<str:country>/<str:rna_or_siren>/'
    getorcreate_admin_suffix = 'getorcreate'

    def getorcreate_view(self, request, country, rna_or_siren, object_id=None, form_url=None, extra_context=None):
        try:
            entity = CompanyModel.objects.get(Q(company_fr__rna=rna_or_siren) | Q(company_fr__siren=rna_or_siren))
            return redirect(f'admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change', object_id=entity.id)
        except CompanyModel.DoesNotExist:
            suffix = self.get_admin_urlname(self.create_admin_suffix)
            return redirect(f'admin:{suffix}', country=country, rna_or_siren=rna_or_siren)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                self.action_admin_path,
                self.wrap(self.action_view, object_tools=self.action_object_tools),
                name=self.get_admin_urlname(self.action_admin_suffix),
            ),
            path(
                self.country_admin_path,
                self.wrap(self.country_view, object_tools=self.country_object_tools),
                name=self.get_admin_urlname(self.country_admin_suffix),
            ),
            path(
                self.search_admin_path,
                self.wrap(self.search_view, object_tools=self.search_object_tools),
                name=self.get_admin_urlname(self.search_admin_suffix),
            ),
            path(
                self.create_admin_path,
                self.wrap(self.create_view),
                name=self.get_admin_urlname(self.create_admin_suffix),
            ),
            path(
                self.getorcreate_admin_path,
                self.wrap(self.getorcreate_view),
                name=self.get_admin_urlname(self.getorcreate_admin_suffix),
            )
        ]
        return my_urls + urls


class CompanyFRAdminInline(admin.StackedInline):
    fields = fields.country + fields.fr
    extra = 0
    max_num = 1


class CompanyAddressFRAdminInline(AddressAdminInline):
    fields = (*address_fields, 'is_siege', 'is_active')


class BaloAdmin(BaseAdmin):
    fieldsets = ((None, {'classes': ('wide',), 'fields': fields.balo}),)
