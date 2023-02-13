from django.db import models
from mighty.models import News
from company.apps import CompanyConfig as conf

class CompanyNews(News):
    company = models.ForeignKey(conf.Model.Company, on_delete=models.CASCADE, related_name='company_news')

    class Meta(News.Meta):
        abstract = True