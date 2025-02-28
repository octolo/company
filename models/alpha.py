from django.db import models

from company import translates as _
from company.apps import CompanyConfig as conf
from mighty.models.base import Base


class CompanyAlpha2(Base):
    company = models.ForeignKey(
        conf.Model.Company, on_delete=models.CASCADE, blank=True, null=True
    )
    denomination = models.CharField(max_length=255)
    since = models.DateField(_.since, blank=True, null=True)

    class Meta(Base.Meta):
        abstract = True

    def far_since(self):
        return
