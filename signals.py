from django.db.models.signals import post_save

from company import get_company_model

CompanyModel = get_company_model()
CompanyFR = get_company_model('CompanyFR')
CompanyAddressFR = get_company_model('CompanyAddressFR')


def DefaultSiegeFR(sender, instance, **kwargs):
    company = instance.company
    if instance.rna:
        company.is_type = 'ASSOCIATION'
    if instance.siege:
        company.siege_fr = instance
        company.save()
    elif not instance.company.siege_fr:
        companyfr = instance.company.company_fr.all().order_by('siege')
        if len(companyfr):
            company.siege_fr = companyfr[0]
            company.save()


post_save.connect(DefaultSiegeFR, CompanyFR)
