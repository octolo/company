from django.db import models
from django.conf import settings
from mighty.models.base import Base
from mighty.applications.address.models import Address
from company import translates as _, choices, managers
from company.apps import CompanyConfig as conf

CHOICES_APE = sorted(list(choices.APE), key=lambda x: x[1])
CHOICES_LEGALFORM = sorted(list(choices.LEGALFORM), key=lambda x: x[1])
class Company(Base):
    search_fields = ['denomination']
    denomination = models.CharField(max_length=255)
    since = models.DateField(_.since, null=True)

    objects = models.Manager()
    objectsB = managers.CompanyManager()

    class Meta(Base.Meta):
        abstract = True
        verbose_name = _.v_company
        verbose_name_plural = _.vp_company
        ordering = ['denomination']

    def __str__(self):
        return "%s (%s)" % (self.denomination, self.siren)

    def arguments(self):
        return {'siren': self.siren}

    @property
    def ape_code(self): return self.ape if self.ape else _.ape_null
    @property
    def ape_label(self): return dict(choices.APE).get(self.ape)
    @property
    def legalform_code(self): return self.legalform if self.legalform else _.legalform_null
    @property
    def legalform_label(self): return dict(choices.LEGALFORM).get(self.legalform)

class CompanyAddress(Address):
    company = models.ForeignKey(conf.ForeignKey.Company, on_delete=models.CASCADE, related_name='company_address')
    nic = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta(Base.Meta):
        abstract = True