from django.db.models.signals import post_save
from company.apps import CompanyConfig as conf
from company import backends_loop, get_company_model

CompanyModel = get_company_model()
CompanyFR = get_company_model("CompanyFR")
CompanyAddressFR = get_company_model("CompanyAddressFR")

def AddressFrInit(sender, instance, **kwargs):
    if not instance.company.companyfr_address.count() or \
        not instance.company.companyfr_address.filter(nic=instance.nic).count():
        message, companies, total, pages = backends_loop('fr', instance.siren)
        if len(companies):
            company_bl = companies[0]
            addressfr, status = CompanyAddressFR.objects.get_or_create(
                company=instance.company,
                is_siege=company_bl['siege'],
                address=company_bl['address']['address'],
                complement=company_bl['address']['complement'],
                postal_code=company_bl['address']['postal_code'],
                locality=company_bl['address']['locality'],
                country=company_bl['address']['country'],
                country_code=company_bl['address']['country_code'],
                nic=company_bl['address']['nic']
            )
            addressfr.save()
#post_save.connect(AddressFrInit, CompanyFR)

def DefaultSiege(sender, instance, **kwargs):
    companyfr = instance.company_fr.all()
    if not instance.siege_fr and companyfr:
        instance.siege_fr = companyfr[0]
        instance.save()
post_save.connect(DefaultSiege, CompanyModel)