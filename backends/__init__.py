from django.conf import settings
from importlib import import_module


default_backends = getattr(settings, 'COMPANY_SEARCH_BACKENDS', (
    'company.backends.search.insee.SearchBackend',
    'company.backends.search.opendatasoft.SearchBackend',
    'company.backends.search.entdatagouv.SearchBackend',
))


def search_company_or_association(search, backends=None):
    results = {}
    for backend in backends or default_backends:
        module, cls = backend.rsplit('.', 1)
        total, results = getattr(import_module(module), cls)().search(search)
        if total and len(results):
            return total, results
    return 0, []
