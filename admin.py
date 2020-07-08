from django.contrib import admin
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.urls import reverse, resolve
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse

from mighty.admin.models import BaseAdmin
from mighty.applications.address import fields as address_fields
from mighty.applications.address.admin import AddressAdminInline


from company import models, fields, translates as _
from company.apps import CompanyConfig as conf

class CompanyAddressAdminInline(AddressAdminInline):
    fields = address_fields + ('nic',)

class CompanyFRAdminInline(admin.StackedInline):
    fields = fields.fr
    extra = 1
    max_num = 1

class CompanyAdmin(BaseAdmin):
    fieldsets = ((None, {'classes': ('wide',), 'fields': fields.company}),)
    list_display = fields.company
    search_fields = ('denomination',)
    change_list_template = 'admin/company_change_list.html'
    search_template = None

    def choices_view(self, request, extra_context=None):
        opts = self.model._meta
        context = {
            **self.admin_site.each_context(request),
            "title": _.countries,
            'object_name': str(opts.verbose_name),
            'countries': [alpha2 for alpha2, backends in settings.COMPANY_BACKENDS.items()],
            'opts': opts,
            'app_label': opts.app_label,
            'media': self.media
        }
        request.current_app = self.admin_site.name
        return TemplateResponse(request, 'admin/company_backends.html', context)

    @never_cache
    def search_view(self, request, country, extra_context=None):
        current_url = resolve(request.path_info).url_name
        opts = self.model._meta
        context = {
            **self.admin_site.each_context(request),
            "app_path": request.get_full_path(),
            "username": request.user.get_username(),
            "current_url": current_url,
            "country": country,
            "title": _.search,
            "fake": self.model(),
            "fake_fr": self.model().get_dataset_by_country('fr')(),
            'opts': opts,
            'app_label': opts.app_label,
            'media': self.media
        }

        from company.forms import CompanySearchForm
        defaults = {
            'extra_context': context,
            'form_class': CompanySearchForm,
            'success_url': current_url,
            'template_name': self.search_template or 'admin/company_search.html',
        }
        from company.views import SearchByCountry
        return SearchByCountry.as_view(**defaults)(request)

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name
        my_urls = [
            path('choices/', self.wrap(self.choices_view), name='%s_%s_choices' % info),
            path('choices/<str:country>/', self.search_view, name='%s_%s_search' % info),
        ]
        return my_urls + urls 

class BaloAdmin(BaseAdmin):
    fieldsets = ((None, {'classes': ('wide',), 'fields': fields.balo}),)