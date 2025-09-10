from django.db import models
from django.utils.translation import gettext_lazy as _
from company.apps import CompanyConfig as conf
from simple_history.models import HistoricalRecords

class CompanyStatus(models.Model):
    company = models.ForeignKey(conf.model_string('Company'), on_delete=models.CASCADE, related_name='company_to_status')
    status = models.ForeignKey(conf.model_string('CompanyStatusConfig'), on_delete=models.CASCADE, related_name='status_to_company')
    config = models.JSONField(blank=True, null=True, verbose_name='Status Configuration')
    history = HistoricalRecords(inherit=True)

    class Meta:
        verbose_name = _('Company Status')
        verbose_name_plural = _('Company Statuses')
        ordering = ['-created_at']
        db_table = conf.companystatus_table
        abstract = True

    @property
    def value(self):
        if self.status.field_type == 'choice' and self.config and 'choice' in self.config:
            return self.config['choice']
        return self.config.get('value') if self.config else None

    def __str__(self):
        return f"{self.company.denomination} - {self.status}: {self.value}"