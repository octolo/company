default_app_config = 'company.apps.CompanyConfig'

from django.apps import apps as django_apps
from django.conf import settings
from django.utils.module_loading import import_string
from mighty.functions import test
from company.apps import CompanyConfig as conf
from company import translates as _

def search_by_siren(backend, siren):
    return backend.get_company_by_siren(siren)

def search_by_fulltext(backend, fulltext):
    return backend.get_company_by_fulltext(fulltext)

def get_backend(backend, search):
    if search.isdigit() and len(search) == 9:
        return search_by_siren(import_string(backend)(), search)
    return search_by_fulltext(import_string(backend)(), search)

def get_backend_data(backend):
    return import_string(backend+".CompanyDataBackend")

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
    message, results, total, pages = ('Nothing', [], 0, 0)
    for backend in settings.COMPANY_BACKENDS[country]:
        message, results, total, pages = get_backend('%s.SearchBackend' % backend, search)
        if total:
            break
    return message, results, total, pages

def get_company_model(address_or_country='Company'):
    return django_apps.get_model(conf.app_label, getattr(conf.Model, address_or_country).lower())

def create_company(country, input_obj):
    from django.utils.module_loading import import_string
    return import_string('company.backends.country.fr.new_company')(input_obj)
    #CompanyModel = get_company_model()
    #CompanyCountry = get_company_model("Company%s" % country.upper())
    #CompanyAddress = get_company_model("CompanyAddress%s" % country.upper())
    ##company, created = CompanyModel.objects.get_or_create(denomination=input_obj['denomination'])
    #address = None
    #if 'address' in input_obj:
    #    address = input_obj['address']
    #    del input_obj['address']
    #del input_obj['ape_str']
    #del input_obj['legalform_str']
    #del input_obj['slice_str']
    #del input_obj['raw_address']
    #data = {key: value for key,value in input_obj.items()}
    #companyC, created = CompanyCountry.objects.get_or_create(**data)
    #if address:
    #    address['company'] = companyC.company
    #    companyA, created = CompanyAddress.objects.get_or_create(**address)
    #return companyC.company


def get_results(country, search):
    message, companies, total, pages = backends_loop(country, search)
    return {
        'search': search,
        'object_list': companies,
        'message': message,
        'total': total,
        'pages': pages,
        'error': False,#cf.message,
        'results': _.results % total if int(total) > 1 else _.result % total,
        'strpages': _.pages % pages if int(pages) > 1 else _.page % pages,
        'toomuch': _.toomuch % total,
    }

def create_at_unique(country, search):
    results = get_results(country, search)
    if len(results['object_list']) == 1:
        data, company = create_company(country.upper(), results['object_list'][0])
        return data
    return {}