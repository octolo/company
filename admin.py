from django.contrib import admin
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib.admin.options import TO_FIELD_VAR
from django.contrib.admin.utils import unquote
from django.urls import reverse, resolve
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse

from mighty.admin.models import BaseAdmin
from mighty.applications.address import fields as address_fields
from mighty.applications.address.admin import AddressAdminInline

from company import models, fields, translates as _
from company.apps import CompanyConfig as conf


class CompanyAdmin(BaseAdmin):
    fieldsets = ((None, {"classes": ("wide",), "fields": fields.company}),)
    list_display = fields.company
    search_fields = ("denomination", "company_fr__siret")
    change_list_template = "admin/company_change_list.html"
    change_form_template = "admin/company_change_form.html"
    change_form_logs_template = "admin/company_change_form_logs.html"
    search_template = None

    def render_change_form(self, request, context, add=False, change=False, form_url="", obj=None):
        response = super().render_change_form(request, context, add, change, form_url, obj)
        if hasattr(self.model, "changelog_model"):
            response.template_name = self.change_form_logs_template
        return response

    def country_choice_view(self, request, object_id=None, extra_context=None):
        current_url = resolve(request.path_info).url_name
        opts = self.model._meta
        to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
        obj = self.get_object(request, unquote(object_id), to_field) if object_id else None
        context = {
            **self.admin_site.each_context(request),
            "current_url": current_url,
            "title": "%s (%s)" % (_.countries, obj) if obj else _.countries,
            "object_name": str(opts.verbose_name),
            "object": obj,
            "opts": opts,
            "app_label": opts.app_label,
            "media": self.media
        }
        request.current_app = self.admin_site.name
        defaults = {
            "extra_context": context,
            "template_name": self.search_template or "admin/company_country_choice.html",
        }
        from company.views import ChoiceCountry
        return ChoiceCountry.as_view(**defaults)(request)

    @never_cache
    def country_search_view(self, request, country, object_id=None, extra_context=None):
        current_url = resolve(request.path_info).url_name
        opts = self.model._meta
        to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
        parent_object = self.get_object(request, unquote(object_id), to_field) if object_id else None
        context = {
            **self.admin_site.each_context(request),
            "parent_object": parent_object,
            "app_path": request.get_full_path(),
            "username": request.user.get_username(),
            "current_url": current_url,
            "country": country,
            "title": _.search,
            "opts": opts,
            "app_label": opts.app_label,
            "media": self.media
        }
        defaults = {
            "extra_context": context,
            "country": country,
            "parent_object": parent_object if parent_object else None,
            "success_url": current_url,
            "template_name": self.search_template or "admin/company_country_search.html",
        }
        from company.views import SearchByCountry
        return SearchByCountry.as_view(**defaults)(request)

    @never_cache
    def country_add_view(self, request, country, object_id=None, extra_context=None):
        current_url = resolve(request.path_info).url_name
        opts = self.model._meta
        to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
        parent_object = self.get_object(request, unquote(object_id), to_field) if object_id else None
        context = {
            **self.admin_site.each_context(request),
            "parent_object": parent_object,
            "app_path": request.get_full_path(),
            "username": request.user.get_username(),
            "current_url": current_url,
            "country": country,
            "title": _.search,
            "opts": opts,
            "app_label": opts.app_label,
            "media": self.media
        }
        defaults = {
            "extra_context": context,
            "admin": True,
            "country": country,
            "parent_object": parent_object if parent_object else None,
            "template_name": self.search_template or "admin/company_country_add.html",
        }
        from company.views import AddByCountry, SearchByCountry
        return AddByCountry.as_view(**defaults)(request)

    def get_urls(self):
        from django.urls import path, include
        urls = super().get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name
        my_urls = [
            path("choices/", include([
                path("", self.country_choice_view, name="%s_%s_country_choice" % info),
                path("<str:country>/search/", include([
                    path("", self.country_search_view, name="%s_%s_country_search" % info),
                    path("add/", self.country_add_view, name="%s_%s_country_add" % info),
                ]))
            ])),
            path("<path:object_id>/choices/", include([
                path("", self.country_choice_view, name="%s_%s_country_choice_extend" % info),
                path("<str:country>/search/", include([
                   path("", self.country_search_view, name="%s_%s_country_search_extend" % info),
                    path("add/", self.country_add_view, name="%s_%s_country_add_extend" % info),
                ]))
            ]))
        ]
        return my_urls + urls 

#####################
# FR
#####################
class CompanyFRAdminInline(admin.StackedInline):
    fields = fields.country + fields.fr
    extra = 0
    max_num = 0

class CompanyAddressFRAdminInline(AddressAdminInline):
    fields = address_fields

class BaloAdmin(BaseAdmin):
    fieldsets = ((None, {"classes": ("wide",), "fields": fields.balo}),)

#####################
# US
#####################