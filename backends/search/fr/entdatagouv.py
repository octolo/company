from company.backends.search.fr import SearchBackendFr


class SearchBackend(SearchBackendFr):
    base_url = 'https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/economicref-france-sirene-v3@public/records'
    urls = {
        'siren': 'https://recherche-entreprises.api.gouv.fr/search?q=%s&is_siege=yes',
        'siret': 'https://recherche-entreprises.api.gouv.fr/search?q=%s&is_siege=yes',
        'rna': 'https://entreprise.data.gouv.fr/api/rna/v1/id/%s?is_siege=yes',
        'text': 'https://recherche-entreprises.api.gouv.fr/search?q=%s&is_siege=yes',
    }

    fields_association = {
        'siren': 'siren',
        'rna': 'id_association',
        'siret': 'siege.siret',
        'denomination': ('nom_complet', 'nom_raison_sociale'),
        'since': ('date_creation', 'date_creation_entreprise'),
        'legalform': 'nature_juridique',
        'ape': 'siege.activite_principale',
        'category': 'categorie_entreprise',
        'slice_effective': 'siege.tranche_effectif_salarie',
        'siege': 'siege.est_siege',
        'locality': 'siege.libelle_commune',
        'postal_code': 'siege.code_postal',
        'cedex': 'siege.cedex',
        'nic': 'siege.nic_siege',
    }

    def get_value_address(self, obj):
        nve = self.getattr_recursive(obj, 'siege.numero_voie')
        tve = self.getattr_recursive(obj, 'siege.type_voie')
        lve = self.getattr_recursive(obj, 'siege.libelle_voie')
        return f'{nve} {tve} {lve}'

    def get_results(self, search, page=1):
        search_type = self.get_search_type(search)
        urls = self.urls.get(search_type) % search
        buffer, code = self.do_request(urls, 'get')
        if str(code)[0] in {'2', '3'}:
            buffer = buffer.json()
            total = buffer.get('total_results', 0)
            results = buffer.get('results', [])
            self._logger.info(f'Found {total} results')
            return total, results
        return 0, []
