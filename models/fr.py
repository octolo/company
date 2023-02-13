from django.db import models
from django.core.exceptions import ValidationError
from mighty.applications.address.models import Address
from mighty.fields import RichTextField
from mighty.models.base import Base

from company import translates as _
from company.apps import CompanyConfig as conf
from company.models.alpha import CompanyAlpha2
from company import choices as _c
from company.choices import fr as choices_fr

CHOICES_APE = sorted(list(choices_fr.APE), key=lambda x: x[1])
CHOICES_LEGALFORM = sorted(list(choices_fr.LEGALFORM), key=lambda x: x[1])
CHOICES_GOVERNANCE = sorted(list(choices_fr.GOVERNANCE), key=lambda x: x[1])
CHOICES_EVALUATION = sorted(list(choices_fr.EVALUATION), key=lambda x: x[1])

class CompanyFR(CompanyAlpha2):
    search_fields = ['denomination', 'siret', 'isin', 'ticker']
    company = models.ForeignKey(conf.Model.Company, on_delete=models.CASCADE, related_name='company_fr', blank=True, null=True)
    siren = models.CharField(max_length=9, blank=True, null=True)
    siret = models.CharField(_.fr_siret, max_length=14, blank=True, null=True)
    rna = models.CharField(max_length=10, blank=True, null=True, unique=True)
    ape = models.CharField(_.fr_ape, max_length=5, blank=True, null=True)
    ape_noun = models.CharField(_.fr_ape_noun, max_length=10, blank=True, null=True)
    category = models.CharField(_.fr_category, max_length=15, blank=True, null=True)
    legalform = models.CharField(_.fr_legalform, max_length=4, blank=True, null=True)
    slice_effective = models.CharField(_.fr_slice_effective, choices=choices_fr.SLICE_EFFECTIVE, blank=True, null=True, max_length=2)
    effective = models.BigIntegerField(_.fr_effective, blank=True, null=True)
    isin = models.CharField(_.fr_isin, max_length=25, blank=True, null=True)
    ticker = models.CharField(_.fr_ticker, max_length=25, blank=True, null=True, db_index=True)
    coderef = models.CharField(_.fr_coderef, max_length=30, choices=choices_fr.CODEREF, blank=True, null=True, db_index=True)
    index = models.CharField(_.fr_index, choices=choices_fr.INDEX, max_length=255, blank=True, null=True, db_index=True)
    governance = models.CharField(_.fr_governance, max_length=255, choices=CHOICES_GOVERNANCE, blank=True, null=True, db_index=True)
    evaluation = models.CharField(_.fr_evaluation, max_length=255, choices=CHOICES_EVALUATION, blank=True, null=True)
    quality_independent = models.CharField(_.fr_quality_independent, max_length=3, choices=_c.YESNO, blank=True, null=True)
    secretary = models.CharField(_.fr_secretary, max_length=255, blank=True, null=True)
    siege = models.BooleanField(default=False)
    resume = RichTextField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    accept_duplicate = False

    class Meta(CompanyAlpha2.Meta):
        abstract = True
        ordering = ['denomination',]

    def __str__(self):
        return self.denomination if hasattr(self, 'denomination') else super().__str__()

    @property
    def date_rcs(self): return self.since
    @property
    def siren_from_siret(self): return self.siret[:9] if self.siret else None
    @property
    def nic(self): return self.siret[9:]
    @property
    def ape_code(self): return self.ape if self.ape else _.ape_null
    @property
    def ape_label(self): return dict(choices_fr.APE).get(self.ape)
    @property
    def slice_label(self): return dict(choices_fr.SLICE_EFFECTIVE).get(self.slice_effective)
    @property
    def legalform_code(self): return self.legalform if self.legalform else _.fr_legalform_null
    @property
    def legalform_label(self): 
        return dict(choices_fr.LEGALFORM).get(int(self.legalform_code)) if self.legalform else _.fr_legalform_null
        
    def check_siret(self):
        if not self.accept_duplicate:
            qs = type(self).objects.filter(siret=self.siret)
            if self.pk: 
                qs = qs.exclude(id=self.id)
            if self.siret and qs.exists():
                raise ValidationError(_.fr_siret_already_used, "siret_already_used")
    
    def clean(self):
        self.check_siret()
        super().clean()

    def save(self, *args, **kwargs):
        self.check_siret()
        try:
            int(self.slice_effective)
        except Exception:
            self.slice_effective = None
        if not self.siren:
            self.siren = self.siren_from_siret
        if self.rna and self.company:
            self.company.is_type = "ASSOCIATION"
            self.company.save()
        super().save()

      
class CompanyAddressFR(Address):
    company = models.ForeignKey(conf.Model.Company, on_delete=models.CASCADE, related_name='companyfr_address')
    nic = models.CharField(max_length=5, blank=True, null=True)
    is_siege = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta(Address.Meta):
        abstract = True
        ordering = ('-is_siege',)

    def __str__(self):
        return self.raw

CHOICES_ANNOUNCE = sorted(list(choices_fr.ANNOUNCE), key=lambda x: x[1])
class Balo(Base):
    companyfr = models.ForeignKey(conf.Model.CompanyFR, on_delete=models.CASCADE)
    announce = models.CharField(choices=CHOICES_ANNOUNCE, max_length=3, null=True)
    case = models.PositiveIntegerField()
    link = models.URLField()
    file_link = models.URLField()
    date = models.DateField()

    class Meta(Base.Meta):
        abstract = True

    def save(self, *args, **kwargs):
        self.date = datetime.datetime.strptime(self.date, conf.Announce.Balo_dateformat).date()
        super().save()