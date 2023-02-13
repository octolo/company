from django.db import models
from mighty.models.base import Base
from company import translates as _, get_company_model
from company.apps import CompanyConfig as conf

class CompanyAlpha2(Base):
    company = models.ForeignKey(conf.Model.Company, on_delete=models.CASCADE, blank=True, null=True)
    denomination = models.CharField(max_length=255)
    since = models.DateField(_.since, blank=True, null=True)

    class Meta(Base.Meta):
        abstract = True

    def far_since(self):
        return 

    def save(self, *args, **kwargs):
        if self.company:
            self.company.save()
        else:
            self.company = get_company_model().objects.create(denomination=self.denomination, since=self.since)
        super().save()