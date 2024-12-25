from django.contrib import admin
from django.urls import path, resolve


from django.db.models import Q
from django.shortcuts import redirect
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib.admin.options import TO_FIELD_VAR
from django.contrib.admin.utils import unquote
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import redirect

from mighty.admin.models import BaseAdmin
from mighty.applications.address import fields as address_fields
from mighty.applications.address.admin import AddressAdminInline

from company import get_company_model
from company.apps import CompanyConfig
from company import models, fields, translates as _
from company.apps import CompanyConfig as conf
from company.backends import search_company_or_association

CompanyModel = get_company_model("Company")


class CompanyAdmin(BaseAdmin):
    fieldsets = (
        (None, {"classes": ("wide",), "fields": (
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
    search_fields = ("denomination", "company_fr__siret")
    readonly_fields = ('siege_fr', 'siege_fr_address')
    search_template = None

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.add_field("Form", fields.form)
        self.add_field('Comex & Purpose', fields.comex_purpose)
        self.add_field('Market', fields.market)
        self.add_field('Rules', fields.rules)
        self.add_field('FR', fields.countryfr)
        if conf.named_id:
            self.add_field('Informations', ('named_id',))
            self.readonly_fields += ('named_id',)

    choice_action_admin_path = "actions/"
    choice_action_admin_suffix = "actions"
    choice_action_admin_template = "admin/company/actions.html"
    choice_action_object_tools = {"name": "Actions", "url": "actions", "list": True}

    def choice_action_view(self, request, *args, **kwargs):
        return self.admincustom_view(request, **{
            "urlname": self.get_admin_urlname(self.choice_action_admin_suffix),
            "template": self.choice_action_admin_template
        })

    choice_country_admin_path = "actions/<str:action>/countries/"
    choice_country_admin_suffix = "countries"
    choice_country_admin_template = "admin/company/countries.html"
    choice_country_object_tools = {"name": "Countries", "url": "countries"}

    def choice_country_view(self, request, action, object_id=None, form_url=None, extra_context=None):
        extra_context = extra_context or {}
        extra_context["action"] = action
        return self.admincustom_view(request, object_id, extra_context, **{
            "urlname": self.get_admin_urlname(self.choice_country_admin_suffix),
            "template": self.choice_country_admin_template
        })

    search_admin_path = "actions/search/countries/<str:country>/"
    search_admin_suffix = "search"
    search_admin_template = "admin/company/search.html"
    search_object_tools = {"name": "Search", "url": "search"}

    def search_view(self, request, country, object_id=None, form_url=None, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            "country": country,
            "search": request.GET.get("q"),
            "results": [],
            "total": 0
        })
        extra_context["country"] = country
        extra_context["search"] = request.GET.get("q")
        if extra_context["search"]:
            total, results = search_company_or_association(extra_context["search"])
            extra_context["results"] = results
            extra_context["total"] = total
        return self.admincustom_view(request, object_id, extra_context, **{
            "urlname": self.get_admin_urlname(self.search_admin_suffix),
            "template": self.search_admin_template
        })

    create_admin_path = "actions/create/countries/<str:country>/<str:rna_or_siren>/"
    create_admin_suffix = "create"
    create_admin_template = "admin/company/create.html"

    def create_view(self, request, country, rna_or_siren, object_id=None, form_url=None, extra_context=None):
        extra_context = extra_context or {}
        total, results = search_company_or_association(rna_or_siren)
        extra_context.update({
            "country": country,
            "rna_or_siren": rna_or_siren,
            "object": results[0],
        })
        if request.method == "POST" and request.POST.get("rna_or_siren") == rna_or_siren:
            import logging
            from company import create_entity
            logging.warning("Create entity")
            create_entity(country, results[0])
        return self.admincustom_view(request, object_id, extra_context, **{
            "urlname": self.get_admin_urlname(self.create_admin_suffix),
            "template": self.create_admin_template
        })

    getorcreate_admin_path = "actions/getorcreate/countries/<str:country>/<str:rna_or_siren>/"
    getorcreate_admin_suffix = "getorcreate"

    def getorcreate_view(self, request, country, rna_or_siren, object_id=None, form_url=None, extra_context=None):
        try:
            entity = CompanyModel.objects.get(Q(company_fr__rna=rna_or_siren) | Q(company_fr__siren=rna_or_siren))
            return redirect("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.model_name), object_id=entity.id)
        except CompanyModel.DoesNotExist:
            suffix = self.get_admin_urlname(self.create_admin_suffix)
            return redirect(f"admin:{suffix}", country=country, rna_or_siren=rna_or_siren)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                self.choice_action_admin_path,
                self.wrap(self.choice_action_view, object_tools=self.choice_action_object_tools),
                name=self.get_admin_urlname(self.choice_action_admin_suffix),
            ),
            path(
                self.choice_country_admin_path,
                self.wrap(self.choice_country_view, object_tools=self.choice_country_object_tools),
                name=self.get_admin_urlname(self.choice_country_admin_suffix),
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
    fields = address_fields + ('is_siege', 'is_active')


class BaloAdmin(BaseAdmin):
    fieldsets = ((None, {"classes": ("wide",), "fields": fields.balo}),)

