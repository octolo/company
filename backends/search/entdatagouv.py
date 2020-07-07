from company.backends.search import SearchBackend
from io import BytesIO
import base64, pycurl, json

class SearchBackend(SearchBackend):
    siren_url = 'https://entreprise.data.gouv.fr/api/sirene/v1/siren/%s'
    fulltext_url = 'https://entreprise.data.gouv.fr/api/sirene/v1/full_text/%s'
    since_format = '%Y%m%d'

    def call_webservice(self, url):
        buffer = BytesIO() 
        c = pycurl.Curl() 
        c.setopt(c.URL, url) 
        c.setopt(c.WRITEDATA, buffer) 
        c.perform() 
        response_code = c.getinfo(c.RESPONSE_CODE) 
        c.close()
        return json.loads(buffer.getvalue()), response_code

    def get_company_by_siren(self, siren):
        companies, total, pages = ([], 0, 0)
        buffer, response_code = self.call_webservice(self.siren_url %siren)
        company = self.companies(buffer.get('siege_social', [buffer]), response_code)
        if not self.message:
            companies.append({
                'siren': company.get('siren'),
                'denomination': company.get('l1_declaree'),
                'category': company.get('categorie_entreprise'),
                'legalform_code': company.get('nature_juridique_entreprise'),
                'legalform_label': self.legalform(company.get('nature_juridique_entreprise')),
                'ape_code': company.get('activite_principale'),
                'ape_label': self.ape(company.get('activite_principale')),
                'street': company.get('l4_declaree'),
                'city': company.get('l6_declaree'),
                'since': self.since(company.get('date_creation')),
                'lastupdate': self.lastupdate(company.get('updated_at')),
            })
            total, pages = (0, 0)
        return companies, total, pages

    def get_company_by_fulltext(self, fulltext):
        companies, total, pages = ([], 0, 0)
        buffer, response_code = self.call_webservice(self.fulltext_url %fulltext)
        if not self.message:
            for company in self.companies(buffer.get('etablissement', [buffer]), response_code):
                companies.append({
                    'siren': company.get('siren'),
                    'denomination': company.get('l1_declaree'),
                    'category': company.get('categorie_entreprise'),
                    'legalform_code': company.get('nature_juridique_entreprise'),
                    'legalform_label': self.legalform(company.get('nature_juridique_entreprise')),
                    'ape_code': company.get('activite_principale'),
                    'ape_label': self.ape(company.get('activite_principale')),
                    'street': company.get('l4_declaree'),
                    'city': company.get('l6_declaree'),
                    'since': self.since(company.get('date_creation')),
                    'lastupdate': self.lastupdate(company.get('updated_at')),
                })
            total = buffer.get('total_results', 0)
            pages = buffer.get('total_pages', 0)
        return companies, total, pages