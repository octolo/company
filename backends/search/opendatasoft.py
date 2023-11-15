from company.backends.search import SearchBackend

import requests

class SearchBackend(SearchBackend):
    api_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/economicref-france-sirene-v3/records"
    since_format = '%Y-%m-%d'
    raw_address = "%(address)s, %(locality)s %(postal_code)s"

    def call_api(self, url, params):
        try:
            response = requests.get(url, params=params)
            return response.json(), response.status_code
        except Exception as e:
            print(f"Error calling API: {e}")
            return None, 500

    def get_company_by_siren(self, siren, number=50, offset=0):
        qreq = f'siren:{siren} and etablissementsiege:"oui"'
        return self._get_by_query(qreq, number, offset)

    def get_company_by_rna(self, rna, number=50, offset=0):
        qreq = f'identifiantassociationunitelegale:{rna} and etablissementsiege:"oui"'
        return self._get_by_query(qreq, number, offset)

    def get_active_company_by_siren(self, siren, number=50, offset=0):
        qreg = f'siren:{siren} and etatadministratifetablissement:"Actif"',
        return self._get_by_query(qreg, number, offset)

    def get_company_by_fulltext(self, text_query, number=50, offset=0):
        if len(text_query) == 10 and text_query[0] == 'W':
            return self.get_company_by_rna(text_query, number, offset)
        qreq = f'"{text_query}"'
        return self._get_by_query(qreq, number, offset)

    def _get_by_query(self, qreq, number=50, offset=0):
        message, items, total, pages = (False, [], 0, 0)
        params = {
            "where": qreq,
        }
        buffer, response_code = self.call_api(self.api_url, params)

        if response_code == 200:
            total = buffer['total_count']
            pages = round(total/number) if total else 0
            new_item = {}
            for record in buffer.get('results', []):
                new_item = {
                    'siren': record.get('siren'),
                    'siret': record.get('siret'),
                    'denomination': record.get('denominationunitelegale'),
                    'legalform': record.get('categoriejuridiqueunitelegale'),
                    'ape': record.get('activiteprincipaleunitelegale').replace('.', ''),
                    'ape_noun': record.get('nomenclatureactiviteprincipaleunitelegale'),
                    'since': self.since(record.get('datecreationunitelegale')),
                    'category': record.get('categorieentreprise', ''),
                    'slice_effective': record.get('trancheeffectifsunitelegale', ''),
                    'siege': True if record.get('etablissementsiege', '').strip().lower() == 'oui' else False,
                    'rna': record.get('identifiantassociationunitelegale', None),
                    'address': {
                        'address': ' '.join(filter(None, [
                            str(record.get('numerovoieetablissement')),
                            record.get('typevoieetablissement'),
                            record.get('libellevoieetablissement')
                        ])),
                        'complement': record.get('complementadresseetablissement', ''),
                        'locality': record.get('libellecommuneetablissement'),
                        'postal_code': record.get('codepostaletablissement'),
                        'country': (record.get('libellepaysetrangeretablissement') or 'france').lower(),
                        'country_code': (record.get('codepaysetrangeretablissement') or 'fr').lower(),
                        'cedex': record.get('libellecedexetablissement', ''),
                        'cedex_code': record.get('codecedexetablissement', ''),
                        'special': record.get('distributionspecialeetablissement', ''),
                        'index': record.get('indicerepetitionetablissement', ''),
                        'nic': record.get('nic')
                    }
                }
            new_item['raw_address'] = self.raw_address % (new_item['address'])
            new_item['ape_str'] = self.get_ape_str(new_item['ape'])
            new_item['legalform_str'] = self.get_legalform_str(new_item['legalform'])
            new_item['slice_str'] = self.get_slice_str(new_item['slice_effective'])
            items.append(new_item)
        else:
            message = f"Error fetching data from API. Response code: {response_code}"

        return message, items, total, pages

