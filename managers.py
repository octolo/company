from django.db import models
#from tenant import queries as q

Prefetch_related = ('company_address',)
class CompanyManager(models.Manager.from_queryset(models.QuerySet)):
    def get_queryset(self):
        return super().get_queryset()\
            .prefetch_related(*Prefetch_related)\
            .annotate()