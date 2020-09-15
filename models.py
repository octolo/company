from django.db import models
from django.conf import settings
from django.utils.module_loading import import_string

from mighty.models.base import Base
from mighty.models.image import Image
from mighty.applications.address.models import Address

from company import translates as _, managers, get_company_model
from company.apps import CompanyConfig as conf
from company.choices import ICB, MARKET, YESNO

from ckeditor.fields import RichTextField


class Company(Base, Image):
    search_fields = ['denomination']
    denomination = models.CharField(max_length=255)
    since = models.DateField(_.since, null=True)
    icb = models.CharField(_.icb, max_length=40, choices=ICB, blank=True, null=True, db_index=True)
    market = models.CharField(_.market, max_length=40, choices=MARKET, blank=True, null=True, db_index=True)
    capital_division = models.JSONField(blank=True, null=True)
    share_capital = models.FloatField(_.share_capital, blank=True, null=True)
    floating = models.FloatField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)
    effective = models.BigIntegerField(blank=True, null=True)
    purpose = models.CharField(_.purpose, max_length=3, choices=YESNO, blank=True, null=True)
    secretary = models.CharField(_.secretary, max_length=255, blank=True, null=True)
    settle_internal = models.BooleanField(_.settle_internal, default=False)
    duration_mandate = models.PositiveSmallIntegerField(_.duration_mandate, blank=True, null=True)
    matrix_skills = models.BooleanField(_.matrix_skills, default=False)
    instance_comex = models.BooleanField(_.instance_comex, default=False)
    age_limit_pdg = models.BooleanField(_.age_limit_pdg, default=False)
    age_limit_dg = models.BooleanField(_.age_limit_dg, default=False)    
    stock_min_rule = models.PositiveIntegerField(_.stock_min_rule, default=0)
    stock_min_status = models.PositiveIntegerField(_.stock_min_status, default=0)
    resume = RichTextField(blank=True, null=True)

    dowjones = ""
    gaia = ""
    nasdaq = ""


    objects = models.Manager()
    objectsB = managers.CompanyManager()

    class Meta(Base.Meta):
        abstract = True
        verbose_name = _.v_company
        verbose_name_plural = _.vp_company
        ordering = ['denomination']

    def __str__(self):
        return self.denomination

    @property
    def country_choice_url(self):
        return self.get_url('country-choice')

    @property
    def country_choice_extend_url(self):
        return self.get_url('country-choice-extend', arguments=self.arguments())

    def country_search_url(self, country):
        return self.get_url('country-search', arguments={'country': country})

    def country_search_extend_url(self, country):
        args = self.arguments()
        args['country'] = country
        return self.get_url('country-search-extend', arguments=args)

    def get_dataset_by_country(self, alpha2):
        return import_string('%s.models.Company%s' % (self.app_label, alpha2.upper()))

class CompanyAlpha2(Base):
    company = models.ForeignKey(conf.Model.Company, on_delete=models.CASCADE)
    denomination = models.CharField(max_length=255)
    since = models.DateField(_.since, null=True)

    class Meta(Base.Meta):
        abstract = True

    def far_since(self):
        return 

    def save(self, *args, **kwargs):
        if self.company_id is None:
            company = get_company_model()(denomination=self.denomination, since=self.since)
            company.save()
        super().save()

#####################
# FR
#####################
from company.choices import fr as choices_fr
CHOICES_APE = sorted(list(choices_fr.APE), key=lambda x: x[1])
CHOICES_LEGALFORM = sorted(list(choices_fr.LEGALFORM), key=lambda x: x[1])
CHOICES_GOVERNANCE = sorted(list(choices_fr.GOVERNANCE), key=lambda x: x[1])
CHOICES_EVALUATION = sorted(list(choices_fr.EVALUATION), key=lambda x: x[1])
class CompanyFR(CompanyAlpha2):
    search_fields = ['denomination', 'siret', 'isin', 'ticker']
    company = models.ForeignKey(conf.Model.Company, on_delete=models.CASCADE, related_name='company_fr')
    siret = models.CharField(_.fr_siret, max_length=14, unique=True)
    ape = models.CharField(_.fr_ape, max_length=5)
    ape_noun = models.CharField(_.fr_ape_noun, max_length=10, blank=True, null=True)
    category = models.CharField(_.fr_category, max_length=15, blank=True, null=True)
    legalform = models.CharField(_.fr_legalform, max_length=4)
    slice_effective = models.CharField(_.fr_slice_effective, choices=choices_fr.SLICE_EFFECTIVE, blank=True, null=True, max_length=2)
    effective = models.BigIntegerField(_.fr_effective, blank=True, null=True)
    isin = models.CharField(_.fr_isin, max_length=25, blank=True, null=True)
    ticker = models.CharField(_.fr_ticker, max_length=25, blank=True, null=True, db_index=True)
    coderef = models.CharField(_.fr_coderef, max_length=30, choices=choices_fr.CODEREF, blank=True, null=True, db_index=True)
    index = models.CharField(_.fr_index, choices=choices_fr.INDEX, max_length=255, blank=True, null=True, db_index=True)
    governance = models.CharField(_.fr_governance, max_length=255, choices=CHOICES_GOVERNANCE, blank=True, null=True, db_index=True)
    evaluation = models.CharField(_.fr_evaluation, max_length=255, choices=CHOICES_EVALUATION, blank=True, null=True)
    quality_independent = models.CharField(_.fr_quality_independent, max_length=3, choices=YESNO, blank=True, null=True)
    secretary = models.CharField(_.fr_secretary, max_length=255, blank=True, null=True)

    resume = RichTextField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    class Meta(Base.Meta):
        abstract = True

    def __str__(self):
        return self.denomination if hasattr(self, 'denomination') else super().__str__()

    @property
    def date_rcs(self): return self.since
    @property
    def siren(self): return self.siret[:9]
    @property
    def nic(self): return self.siret[10:]
    @property
    def ape_code(self): return self.ape if self.ape else _.ape_null
    @property
    def ape_label(self): return dict(choices_fr.APE).get(self.ape)
    @property
    def legalform_code(self): return self.legalform if self.legalform else _.legalform_null
    @property
    def legalform_label(self): return dict(choices_fr.LEGALFORM).get(self.legalform)

    def save(self, *args, **kwargs):
        try:
            int(self.slice_effective)
        except Exception:
            self.slice_effective = None
        super().save()
      
class CompanyAddressFR(Address):
    companyfr = models.ForeignKey(conf.Model.CompanyFR, on_delete=models.CASCADE, related_name='companyfr_address')

    class Meta(Base.Meta):
        abstract = True

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

#####################
# US
#####################