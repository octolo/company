from django.db import models
from company.apps import CompanyConfig
from company import queries

Prefetch_related = ('company_fr',)
class CompanyManager(models.Manager.from_queryset(models.QuerySet)):
    def get_queryset(self):
        return super().get_queryset()\
            .prefetch_related(*Prefetch_related)\
            .annotate()

