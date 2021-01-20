default_app_config = 'company.apps.CompanyConfig'

from django.apps import apps as django_apps
from django.conf import settings
from django.utils.module_loading import import_string
from mighty.functions import test
from company.apps import CompanyConfig as conf

def search_by_siren(backend, siren):
    return backend.get_company_by_siren(siren)

def search_by_fulltext(backend, fulltext):
    return backend.get_company_by_fulltext(fulltext)

def get_backend(backend, search):
    if search.isdigit() and len(search) == 9:
        return search_by_siren(import_string(backend)(), search)
    return search_by_fulltext(import_string(backend)(), search)

def merge_company(backends):
    base = {}
    for pos, datas in enumerate(backends):
        for key,data in datas.items():
            if data:
                if key in base and data != base[key] and datas['lastupdate'] > base['lastupdate'][0]:
                    base[key] = (data, datas['lastupdate'])
                else:
                    base[key] = (data, datas['lastupdate'])
    return {key: value[0] for key, value in base.items()}

def merge_backends(results):
    return [merge_company([datas for backend, datas in backends.items()]) for company, backends in results.items()]

def backends_loop(country, search):
    results = {}
    ftotal, fpages = (0, 0)
    for backend in settings.COMPANY_BACKENDS[country]:
        return get_backend('%s.SearchBackend' % backend, search)
        #try:
        #    return get_backend('%s.SearchBackend' % backend, search)
        #except Exception as e:
        #    print(e)
    return False
    return merge_backends(results), ftotal, fpages

def get_company_model(address_or_country='Company'):
    return django_apps.get_model(conf.app_label, getattr(conf.Model, address_or_country).lower())

def create_company(country, input_obj):
    CompanyModel = get_company_model()
    CompanyCountry = get_company_model("Company%s" % country.upper())
    CompanyAddress = get_company_model("CompanyAddress%s" % country.upper())
    company, created = CompanyModel.objects.get_or_create(denomination=input_obj['denomination'])
    if 'address' in input_obj:
        del input_obj['address']
    data = {key: value for key,value in input_obj.items()}
    data['company'] = company
    companyC, created = CompanyCountry.objects.get_or_create(**data)
    company.since = input_obj['since']
    company.save()
