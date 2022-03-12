from django.contrib import admin
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib.admin.options import TO_FIELD_VAR
from django.contrib.admin.utils import unquote
from django.urls import reverse, resolve
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import redirect

from mighty.admin.models import BaseAdmin
from mighty.applications.address import fields as address_fields
from mighty.applications.address.admin import AddressAdminInline

from company import get_company_model, get_backend_data
from company.apps import CompanyConfig
from company import models, fields, translates as _
from company.apps import CompanyConfig as conf

class CompanyAdmin(BaseAdmin):
    fieldsets = (
        (None, {"classes": ("wide",), "fields": (
            'denomination',
            'is_type',
            'since',
            'site',
            'effective',
            'secretary',
            'resume',
            'stackholder_kind',
            'stock_kind',
        )}),
        ('comex & purpose', {"classes": ("wide",), "fields": ('purpose', 'instance_comex', 'matrix_skills')}),
        ('market', {"classes": ("wide",), "fields": (
            'capital_socnomtotal',
            'capital_division',
            'current',
            'share_capital',
            'turnover',
            'floating',
            'icb',
            'market',
            'dowjones',
            'nasdaq',
            'gaia'
        )}),
        ('rules', {"classes": ("wide",), "fields": (
            'duration_mandate',
            'settle_internal',
            'age_limit_pdg',
            'age_limit_dg',
            'stock_min_rule',
            'stock_min_status'
        )}),
        ('sieges', {"classes": ("wide",), "fields": (
            'siege_fr',
        )}))

    list_display = ('denomination', 'since', 'siege_fr')
    search_fields = ("denomination", "company_fr__siret")
    change_list_template = "admin/company_change_list.html"
    change_form_template = "admin/company_change_form.html"
    change_form_logs_template = "admin/company_change_form_logs.html"
    readonly_fields = ('siege_fr',)
    search_template = None

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        if conf.named_id:
            self.readonly_fields += ('named_id',)
            self.add_field('Informations', ('named_id',))

    def is_from_update(self, request, obj, response):
        backend = request.GET.get("update_from")
        country = request.GET.get("country")
        country_id = request.GET.get("country_id")
        if backend and country and country_id:
            from django.shortcuts import redirect
            name = "admin:%s_%s_update_from" % (self.model._meta.app_label, self.model._meta.model_name)
            return redirect(name, object_id=obj.id, country=country, country_id=country_id, backend=backend)
        return response

    def render_change_form(self, request, context, add=False, change=False, form_url="", obj=None):
        response = super().render_change_form(request, context, add, change, form_url, obj)
        if hasattr(self.model, "changelog_model"):
            response.template_name = self.change_form_logs_template
        return self.is_from_update(request, obj, response)

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

    #@never_cache
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
        return SearchByCountry.as_view(**defaults)(request=request)

    #@never_cache
    def update_from_view(self, request, object_id, backend, country, country_id, extra_context=None):
        opts = self.model._meta
        to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
        obj = self.get_object(request, unquote(object_id), to_field) if object_id else None
        backend = backend

        from company import get_company_model, get_backend_data
        from company.apps import CompanyConfig
        cmodel = get_company_model('Company%s' % country.upper())
        backend_object = cmodel.objects.get(id=country_id)
        backend_path = "company.backends.data.%s" % backend
        backend_script = get_backend_data(backend_path)(obj=backend_object)
        ndata = {}
        for data in CompanyConfig.FR.list_to_set:
            ndata[data] = backend_script.get_one_data(data)

        context = {
            **self.admin_site.each_context(request),
            'object_name': str(opts.verbose_name),
            'object': obj,
            'backend': backend,
            'opts': opts,
            'app_label': opts.app_label,
            'media': self.media,
            'title': backend,
            'ndata': ndata,
        }
        request.current_app = self.admin_site.name
        return TemplateResponse(request, 'admin/company_update_from.html', context)

    #@never_cache
    def valid_update_from_view(self, request, object_id, backend, country, country_id, extra_context=None):
        opts = self.model._meta
        to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
        obj = self.get_object(request, unquote(object_id), to_field) if object_id else None
        backend = backend
        cmodel = get_company_model('Company%s' % country.upper())
        backend_object = cmodel.objects.get(id=country_id)
        backend_path = "company.backends.data.%s" % backend
        backend_script = get_backend_data(backend_path)(obj=backend_object)
        ndata = {}
        for data in CompanyConfig.FR.list_to_set:
            backend_script.set_one_data(data)
        backend_script.save()
        name = "admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.model_name)
        return redirect(name, object_id=obj.id)


    #@never_cache
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
        from company.views import AddByCountry
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
            ])),
            path('<path:object_id>/update/<str:backend>/<str:country>/', include([
                path("<int:country_id>/", self.wrap(self.update_from_view), name='%s_%s_update_from' % info),
                path("<int:country_id>/valid/", self.wrap(self.valid_update_from_view), name='%s_%s_valid_from' % info),
                
            ])),
        ]
        return my_urls + urls

#####################
# FR
#####################
class CompanyFRAdminInline(admin.StackedInline):
    fields = fields.country + fields.fr
    extra = 0
    max_num = 1

class CompanyAddressFRAdminInline(AddressAdminInline):
    fields = address_fields + ('is_siege', 'is_active')

class BaloAdmin(BaseAdmin):
    fieldsets = ((None, {"classes": ("wide",), "fields": fields.balo}),)

#####################
# US
#####################