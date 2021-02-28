from django.db import models
from company.apps import CompanyConfig
from company import queries

Select_related = ('siege_fr',)
class CompanyManager(models.Manager.from_queryset(models.QuerySet)):
    def get_queryset(self):
        return super().get_queryset()\
            .select_related(*Select_related)\
            .annotate(countid=models.Count('id')).order_by('denomination')

