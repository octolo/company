from django.conf import settings
from company.backends.search.fr import SearchBackendFr


class SearchBackend(SearchBackendFr):
    base_url = "https://api.insee.fr/"
    headers = {'Accept': 'application/json', "X-INSEE-Api-Key-Integration": settings.INSEE_API_KEY}
    urls = {
        "siren": {
            "url": "api-sirene/3.11/siret",
            "query": "siren:%s+AND+etatAdministratifUniteLegale:A+AND+etablissementSiege:true",
        },
        "siret": {
            "url": "api-sirene/3.11/siret",
            "query": "siret:%s+AND+etatAdministratifUniteLegale:A+AND+etablissementSiege:true",
        },
        "rna": {
            "url": "api-sirene/3.11/siret",
            "query": "identifiantAssociationUniteLegale:%s+AND+etablissementSiege:true+AND+etatAdministratifUniteLegale:A",
        },
        "text": {
            "url": "api-sirene/3.11/siret",
            "query": "denominationUniteLegale:%s+AND+etatAdministratifUniteLegale:A+AND+etablissementSiege:true",
        },
    }

    fields_association = {
        "siren": "siren",
        "rna": "uniteLegale.identifiantAssociationUniteLegale",
        "denomination": (
            "uniteLegale.denominationUniteLegale",
            "uniteLegale.nomUniteLegale"
        ),
        "ape": "uniteLegale.activitePrincipaleUniteLegale",
        "legalform": "uniteLegale.categorieJuridiqueUniteLegale",
        "ape_noun": "uniteLegale.nomenclatureActivitePrincipaleUniteLegale",
        "since": "uniteLegale.dateCreationUniteLegale",
        "category": "uniteLegale.categorieEntreprise",
        "slice_effective": "uniteLegale.trancheEffectifsUniteLegale",
        "siege": "etablissementSiege",
        "complement": "adresseEtablissement.complementAdresseEtablissement",
        "locality": (
            "adresseEtablissement.libelleCommuneEtablissement",
            "adresseEtablissement.libelleCommuneEtrangerEtablissement"
        ),
        "postal_code": (
            "adresseEtablissement.codePostalEtablissement",
            "adresseEtablissement.codeCommuneEtablissement",
        ),
        "country": "adresseEtablissement.libellePaysEtrangerEtablissement",
        "country_code": "adresseEtablissement.codePaysEtrangerEtablissement",
        "cedex": "adresseEtablissement.libelleCedexEtablissement",
        "cedex_code": "adresseEtablissement.codeCedexEtablissement",
        "special": "adresseEtablissement.distributionSpecialeEtablissement",
        "index": "adresseEtablissement.indiceRepetitionEtablissement",
    }

    def get_value_address(self, obj):
        nve = self.getattr_recursive(obj, "adresseEtablissement.numeroVoieEtablissement")
        tve = self.getattr_recursive(obj, "adresseEtablissement.typeVoieEtablissement")
        lve = self.getattr_recursive(obj, "adresseEtablissement.libelleVoieEtablissement")
        return f"{nve} {tve} {lve}"

    def get_results(self, search, page=1):
        search_type = self.get_search_type(search)
        search_conf = self.urls.get(search_type)
        query = f"?q={search_conf['query'] % search}&nombre={self.show_by_page}&debut={self.show_by_page * (page - 1)}&masquerValeursNulles=true"
        url = f"{self.base_url}{search_conf['url']}{query}"
        self._logger.debug(f"URL: {url}")
        buffer, code = self.do_request(url, "get", headers=self.headers)
        if str(code)[0] in ["2", "3"]:
            buffer = buffer.json()
            total = buffer.get("header", {}).get("total")
            results = buffer.get("etablissements", [])
            self._logger.info(f"Found {total} results")
            return total, results
        return 0, []
