from django.db import models
from django.conf import settings
from mighty.models.base import Base
from mighty.applications.address.models import Address
from company import translates as _, choices, managers
from company.apps import CompanyConfig as conf
from django.utils.module_loading import import_string

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
        return self.denomination

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

    def get_dataset_by_country(self, alpha2):
        return import_string('%s.models.Company%s' % (self.app_label, alpha2.upper()))

class CompanyAddress(Address):
    company = models.ForeignKey(conf.ForeignKey.Company, on_delete=models.CASCADE, related_name='company_address')
    nic = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta(Base.Meta):
        abstract = True

"""
FR
"""
CHOICES_APE = sorted(list(choices.APE), key=lambda x: x[1])
CHOICES_LEGALFORM = sorted(list(choices.LEGALFORM), key=lambda x: x[1])
class CompanyFR(Base):
    company = models.ForeignKey(conf.ForeignKey.Company, on_delete=models.CASCADE, related_name='company_fr')
    denomination = models.CharField(max_length=255)
    since = models.DateField(_.since, null=True)
    siren = models.CharField(max_length=9, unique=True)
    ape = models.CharField(_.corebusiness, max_length=5)
    legalform = models.CharField(_.legalform, max_length=4)

    class Meta(Base.Meta):
        abstract = True

    def __str__(self):
        return self.company.denomination

CHOICES_ANNOUNCE = sorted(list(choices.ANNOUNCE), key=lambda x: x[1])
class Balo(Base):
    announce = models.CharField(choices=CHOICES_ANNOUNCE, max_length=3, null=True)
    company = models.ForeignKey(conf.ForeignKey.Company, on_delete=models.CASCADE)
    case = models.PositiveIntegerField()
    link = models.URLField()
    file_link = models.URLField()
    date = models.DateField()

    class Meta(Base.Meta):
        abstract = True

    def save(self, *args, **kwargs):
        self.date = datetime.datetime.strptime(self.date, conf.Announce.Balo_dateformat).date()
        super().save()

