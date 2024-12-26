from django.conf import settings
from importlib import import_module


search_backends = getattr(settings, 'COMPANY_SEARCH_BACKENDS', {
    "fr": [
        "company.backends.search.fr.insee.SearchBackend",
        "company.backends.search.fr.opendatasoft.SearchBackend",
        "company.backends.search.fr.entdatagouv.SearchBackend",
    ],
})


def search_entity(country, search, backends=None):
    results = {}
    backends = backends or search_backends
    country_backends = backends.get(country, [])
    for backend in country_backends:
        module, cls = backend.rsplit('.', 1)
        total, results = getattr(import_module(module), cls)().search(search)
        if total and len(results):
            return total, results
    return 0, []
