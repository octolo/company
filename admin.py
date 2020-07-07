from django.contrib import admin
from django.conf import settings
from mighty.admin.models import BaseAdmin
from company import models, fields
from company.apps import CompanyConfig as conf
from mighty.applications.address import fields as address_fields
from mighty.applications.address.admin import AddressAdminInline

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

class BaloAdmin(BaseAdmin):
    fieldsets = ((None, {'classes': ('wide',), 'fields': fields.balo}),)