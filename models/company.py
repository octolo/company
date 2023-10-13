from django.db import models
from django.conf import settings
from django.utils.module_loading import import_string
from django.utils.html import format_html
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

from mighty.models import News
from mighty.models.base import Base
from mighty.models.image import Image
from mighty.applications.address.models import Address
from mighty.fields import RichTextField

from company import translates as _, managers, get_company_model
from company.apps import CompanyConfig as conf
from company import choices as _c
from company.notify import SlackCompany, DiscordCompany

class Company(Base, Image):
    rules_fields = ["settle_internal", "duration_mandate", "age_limit_pdg", "age_limit_dg", "stock_min_rule", "stock_min_status"]
    marketplace_fields = ["capital_division", "current", "share_capital", "icb", "market", "dowjones", "nasdaq", "gaia"]
    infos_fields = ["purpose", "instance_comex", "matrix_skills"]
    search_fields = ['denomination']

    denomination = models.CharField(max_length=255)
    since = models.DateField(_.since, null=True)
    site = models.URLField(blank=True, null=True)
    effective = models.BigIntegerField(blank=True, null=True)
    secretary = models.CharField(_.secretary, max_length=255, blank=True, null=True)
    resume = RichTextField(blank=True, null=True)

    is_type = models.CharField(max_length=15, choices=_c.ISTYPE, default="COMPANY")

    purpose = models.CharField(_.purpose, max_length=3, choices=_c.YESNO, blank=True, null=True)
    instance_comex = models.BooleanField(_.instance_comex, default=False)
    matrix_skills = models.BooleanField(_.matrix_skills, default=False)

    capital_socnomtotal = models.DecimalField(_.capital_socnomtotal, blank=True, null=True, decimal_places=2, max_digits=15)
    capitalisation = models.DecimalField(_.capitalisation, decimal_places=2, max_digits=15, default=0.0)
    nominal = models.DecimalField(_.nominal, decimal_places=2, max_digits=15, default=0.0)
    turnover = models.BigIntegerField(_.turnover, blank=True, null=True)
    net_profit = models.BigIntegerField(_.net_profit, blank=True, null=True, help_text=_.net_profit_help)
    dividend = models.FloatField(_.total_dividend, blank=True, null=True)
    securities = models.BigIntegerField(_.securities, blank=True, null=True)
    current = models.FloatField(_.current, default=0.0)
    total_dividend = models.IntegerField(_.total_dividend, blank=True, null=True, help_text=_.total_dividend_help)

    capital_division = models.JSONField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)
    share_capital = models.FloatField(_.share_capital, blank=True, null=True)
    floating = models.FloatField(blank=True, null=True)
    icb = models.CharField(_.icb, max_length=40, choices=_c.ICB, blank=True, null=True, db_index=True)
    market = models.CharField(_.market, max_length=40, choices=_c.MARKET, blank=True, null=True, db_index=True)
    dowjones = models.BooleanField(default=False)
    nasdaq = models.BooleanField(default=False)
    gaia = models.BooleanField(default=False)

    settle_internal = models.BooleanField(_.settle_internal, default=False)
    duration_mandate = models.PositiveSmallIntegerField(_.duration_mandate, blank=True, null=True)
    age_limit_pdg = models.BooleanField(_.age_limit_pdg, default=False)
    age_limit_dg = models.BooleanField(_.age_limit_dg, default=False)
    stock_min_rule = models.PositiveIntegerField(_.stock_min_rule, blank=True, null=True)
    stock_min_status = models.PositiveIntegerField(_.stock_min_status, blank=True, null=True)
    stackholder_kind = models.CharField(max_length=20, choices=_c.STACKHOLDER_KINDS, default=_c.STACKHOLDER_SHAREHOLDER, blank=True, null=True)
    stock_kind = models.CharField(max_length=20, choices=_c.STOCK_KINDS, default=_c.STOCK_SHAREHOLDER, blank=True, null=True)

    siege_fr = models.ForeignKey(conf.Model.CompanyFR, on_delete=models.CASCADE, related_name='siege_fr', blank=True, null=True)

    if conf.named_id:
        named_id = models.CharField(max_length=255, db_index=True, null=True, editable=False)

    objects = models.Manager()
    objectsB = managers.CompanyManager()

    class Meta(Base.Meta):
        abstract = True
        verbose_name = _.v_company
        verbose_name_plural = _.vp_company
        ordering = ['denomination']

    @property
    def slack_notify(self): return SlackCompany(self)
    @property
    def discord_notify(self): return DiscordCompany(self)


    def set_floating(self):
        try:
            self.floating = float(self.capital_division['Flottant'])
        except Exception:
            pass

    def set_named_id(self, offset=0):
        if hasattr(self, 'named_id'):
            self.named_id = conf.named_tpl % {"named": slugify(self.denomination), "id": self.siren_or_rna}
            if offset: self.named_id += "-"+str(offset)
            qs = self.model.objects.filter(named_id=self.named_id)
            if self.pk: qs = qs.exclude(pk=self.pk)
            if len(qs): self.set_named_id(offset+1)

    def post_create(self):
        self.slack_notify.send_msg_create()
        self.discord_notify.send_msg_create()

    def pre_update(self):
        self.set_siege_fr()
        self.set_floating()
        self.set_named_id()
        self.set_stackholder_kind()
        self.set_stock_kind()
        self.prepare_kind()

    def __str__(self):
        return self.denomination

    @property
    def infos(self): return {f: getattr(self, f) for f in self.infos_fields}
    @property
    def rules(self): return {f: getattr(self, f) for f in self.rules_fields}
    @property
    def marketplace(self):
        data = {f: getattr(self, f) for f in self.marketplace_fields}
        data.update({"floating": round(self.floating, 2) if self.floating else None})
        return data
    @property
    def capital_text(self): return format_html('200 000 €<br/>');
    @property
    def capital_var_text(self): return format_html('500 000 €<br/>');

    @property
    def country_choice_url(self): return self.get_url('country-choice')
    @property
    def country_choice_extend_url(self): return self.get_url('country-choice-extend', arguments=self.arguments())

    def country_search_url(self, country):
        return self.get_url('country-search', arguments={'country': country})

    def country_search_extend_url(self, country):
        args = self.arguments()
        args['country'] = country
        return self.get_url('country-search-extend', arguments=args)

    def get_dataset_by_country(self, alpha2):
        return import_string('%s.models.Company%s' % (self.app_label, alpha2.upper()))

    @property
    def siege_or_first_fr(self): return self.siege_fr if self.siege_fr_id else self.company_fr.first()
    @property
    def siege_fr_address(self): return self.companyfr_address.order_by('-is_siege').first()


    # KIND
    @property
    def stock_name(self): return self.get_stock_kind_display()
    @property
    def stock_name_min(self): return self.get_stock_kind_display().lower()
    @property
    def stackholder_name(self): return self.get_stackholder_kind_display()
    @property
    def is_association(self): return (self.is_type == _c.ASSOCIATION)
    @property
    def kind(self): return "association" if self.is_association else "entreprise"

    def stock_kind_default(self, legalform=None):
        if legalform and str(legalform) in _c.STOCK_DEFAULT:
            return _c.STOCK_DEFAULT[str(legalform)]
        return _c.STOCK_SHAREHOLDER

    def set_stackholder_kind(self):
        if not self.stackholder_kind:
            fr_data = self.siege_or_first_fr
            if fr_data:
                self.stackholder_kind = self.stackholder_kind_default(fr_data.legalform)

    def stackholder_kind_default(self, legalform=None):
        if legalform and str(legalform) in _c.STACKHOLDER_DEFAULT:
            return _c.STACKHOLDER_DEFAULT[str(legalform)]
        return _c.STACKHOLDER_SHAREHOLDER

    def set_stock_kind(self):
        if not self.set_stock_kind:
            fr_data = self.siege_or_first_fr
            if fr_data:
                self.stock_kind = self.stock_kind_default(fr_data.legalform)

    def prepare_kind(self):
        if self.is_type == _c.ASSOCIATION:
            self.stock_kind = _c.STOCK_VOICE
            self.stackholder_kind = _c.STACKHOLDER_MEMBER
        elif self.is_type == _c.COOWNER:
            self.stock_kind = _c.STOCK_SHARES
            self.stackholder_kind = _c.STACKHOLDER_OWNER
        #elif self.is_type == _c.BIGMASTER:
        #    self.stock_kind = STOCK_TITLE
        #    self.stackholder_kind = _c.STACKHOLDER_ASSOCIATE

    # FR
    @property
    def isin(self): return self.siege_or_first_fr.isin
    @property
    def siren(self): return self.siege_or_first_fr.siren
    @property
    def rna(self): return self.siege_or_first_fr.rna
    @property
    def index(self): return self.siege_or_first_fr.index
    @property
    def siren_or_rna(self):
        if self.siege_or_first_fr:
            return self.rna if self.rna else self.siren
        return "n-a"

    def set_siege_fr(self):
        try:
            self.siege_fr = self.company_fr.get(siege=True)
        except Exception:
            pass

    # ADDRESS
    @property
    def raw_address(self):
        first_address = self.companyfr_address.first()
        return first_address.raw if first_address else None
