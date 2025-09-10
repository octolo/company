from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from simple_history.models import HistoricalRecords

class CompanyStatusFieldType(models.TextChoices):
    STRING = 'string', _('String')
    INTEGER = 'integer', _('Integer')
    BOOLEAN = 'boolean', _('Boolean')
    DATE = 'date', _('Date')
    CHOICE = 'choice', _('Choice')
    FLOAT = 'float', _('Float')

class CompanyStatusConfig(models.Model):
    country = CountryField(verbose_name='Country', blank_label='(Select country)', null=True, blank=True)
    code = models.CharField(max_length=255, verbose_name='Status Code')
    label = models.CharField(max_length=255, verbose_name='Status Label')
    field_type = models.CharField(max_length=50, choices=CompanyStatusFieldType.choices, default=CompanyStatusFieldType.STRING, verbose_name='Field Type')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    config = models.JSONField(blank=True, null=True, verbose_name='Configuration (for choices, etc.)')
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    history = HistoricalRecords(inherit=True)

    class Meta:
        verbose_name = _('Company Status Configuration')
        verbose_name_plural = _('Company Status Configurations')
        ordering = ['-created_at']
        db_table = conf.companystatusconfig_table
        abstract = True