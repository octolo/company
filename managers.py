from django.db import models

Select_related = ('siege_fr',)


class CompanyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .select_related(*Select_related)\
            .annotate(countid=models.Count('id'))\
            .order_by('denomination')
