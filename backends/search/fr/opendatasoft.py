from company.backends.search.fr import SearchBackendFr


class SearchBackend(SearchBackendFr):
    base_url = "https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/economicref-france-sirene-v3@public/records"
    urls = {
        "siren": "siren:\"%s\" and etablissementsiege:\"oui\" and etatadministratifetablissement:\"Actif\"",
        "siret": "siret:\"%s\" and etablissementsiege:\"oui\" and etatadministratifetablissement:\"Actif\"",
        "rna": "identifiantassociationunitelegale:\"%s\" and etablissementsiege:\"oui\" and etatadministratifetablissement:\"Actif\"",
        "text": "\"%s\" and etablissementsiege:\"oui\" and etatadministratifetablissement:\"Actif\"",
    }

    fields_association = {
        "siren": "siren",
        "rna": "identifiantassociationunitelegale",
        "denomination": "denominationunitelegale",
        "legalform": "categoriejuridiqueunitelegale",
        "ape": "activiteprincipaleunitelegale",
        "ape_noun": "nomenclatureactiviteprincipaleunitelegale",
        "since": "datecreationunitelegale",
        "category": "categorieentreprise",
        "slice_effective": "trancheeffectifsunitelegale",
        "complement": "complementadresseetablissement",
        "locality": "libellecommuneetablissement",
        "postal_code": "codepostaletablissement",
        "country": "libellepaysetrangeretablissement",
        "country_code": "codepaysetrangeretablissement",
        "cedex": "libellecedexetablissement",
        "cedex_code": "codecedexetablissement",
        "special": "distributionspecialeetablissement",
        "index": "indicerepetitionetablissement",
    }

    def get_value_siege(self, obj):
        return True if obj.get("etablissementsiege", "").strip().lower() == "oui" else False

    def get_value_address(self, obj):
        nve = self.getattr_recursive(obj, "numerovoieetablissement")
        tve = self.getattr_recursive(obj, "typevoieetablissement")
        lve = self.getattr_recursive(obj, "libellevoieetablissement")
        return f"{nve} {tve} {lve}"

    def get_results(self, search, page=1):
        search_type = self.get_search_type(search)
        params = {
            "where": self.urls.get(search_type) % search,
            "limit": self.show_by_page,
            "offset": (page - 1) * self.show_by_page,
        }
        buffer, code = self.do_request(self.base_url, "get", params=params)
        if str(code)[0] in ["2", "3"]:
            buffer = buffer.json()
            total = buffer.get("total_count", 0)
            results = buffer.get("results", [])
            self._logger.info(f"Found {total} results")
            return total, results
        return 0, []
