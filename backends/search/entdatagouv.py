from company.backends.search import SearchBackend
from io import BytesIO
import base64, requests, json, re, logging

logger = logging.getLogger(__name__)

class SearchBackend(SearchBackend):
    siren_url = 'https://recherche-entreprises.api.gouv.fr/search?q=%s&is_siege=yes'
    fulltext_url = 'https://recherche-entreprises.api.gouv.fr/search?q=%s&is_siege=yes'
    rna_url = 'https://entreprise.data.gouv.fr/api/rna/v1/id/%s?is_siege=yes'
    rna_fulltext_url = 'https://entreprise.data.gouv.fr/api/rna/v1/full_text/%s?is_siege=yes'
    since_format = '%Y-%m-%d'
    raw_address = "%(address)s, %(locality)s %(postal_code)s"

    def call_webservice(self, url):
        self.logger.info(url)
        try:
            buffer = requests.get(url)
            return buffer.json(), buffer.status_code
        except Exception as e:
            raise e

    def get_date_creation(self, company):
        date = company.get('date_creation',  company.get('date_creation_entreprise', None))
        return self.since(date) if date else None

    def get_companies(self, url, qreq):
        message, companies, total, pages = (False, [], 0, 0)
        buffer, response_code = self.call_webservice(url % qreq)
        if url == self.siren_url:
            list_company = self.companies(buffer.get('resuelts', [buffer]), response_code)
        elif url == self.rna_url:
            list_company = self.companies(buffer.get('association', [buffer]), response_code)
        else:
            list_company = self.companies(buffer.get('etablissement', [buffer]), response_code)
        if not self.message:
            for company in list_company:
                siege = company.get("siege")
                new_company = {
                    'siret': siege.get('siret', None),
                    'denomination': company.get('nom_raison_sociale', None),
                    'legalform': company.get('nature_juridique', None),
                    'ape': company.get('activite_principale', None),
                    'ape_noun': None,
                    'since': self.get_date_creation(company),
                    'category': company.get('categorie_entreprise', None),
                    'slice_effective':  company.get('tranche_effectif_salarie', None),
                    'siege': int(siege.get('est_siege', False)),
                    'rna': siege.get('id_association', None),
                    'address': {
                        'address': ' '.join(filter(None, [
                            siege.get("numero_voie", None),
                            siege.get("type_voie", None),
                            siege.get("libelle_voie", None),
                        ])),
                        'complement': None,
                        'locality': siege.get("libelle_commune", None),
                        'postal_code': siege.get("code_postal", None),
                        'country': 'france',
                        'country_code': 'fr',
                        'cedex': siege.get("cedex", None),
                        'cedex_code': None,
                        'special': None,
                        'index': None,
                        'nic': siege.get('nic_siege')
                    }
                }
                new_company['raw_address'] = self.raw_address % (new_company['address'])
                new_company['ape_str'] = self.get_ape_str(new_company['ape'])
                new_company['legalform_str'] = self.get_legalform_str(new_company['legalform'])
                new_company['slice_str'] = self.get_slice_str(new_company['slice_effective'])
                if new_company["siege"]:
                    companies.append(new_company)
            total = buffer.get('total_results', 0)
            pages = buffer.get('total_pages', 0)
        return message, companies, total, pages

    def get_company_by_siren(self, siren):
        return self.get_companies(self.siren_url, siren)

    #def get_active_companies(self, number, offset):
    #    return self.get_companies('etatAdministratifUniteLegale:A', number, offset)

    def get_company_by_rna(self, rna):
        return self.get_companies(self.rna_url, rna)

    def get_company_by_fulltext(self, fulltext):
        if len(fulltext) == 10 and fulltext[0] == 'W':
            self.get_company_by_rna(fulltext)
        fulltext = re.sub(r"\s+", '-', fulltext)
        return self.get_companies(self.fulltext_url, fulltext)