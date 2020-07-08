from django.conf import settings
from company.backends.search import SearchBackend
from io import BytesIO
import base64, pycurl, json, re
from mighty.functions import get_logger
logger = get_logger()

class SearchBackend(SearchBackend):
    token_url = 'https://api.insee.fr/token'
    siren_url = 'https://api.insee.fr/entreprises/sirene/V3/siren'
    siret_url = 'https://api.insee.fr/entreprises/sirene/V3/siret'
    since_format = '%Y-%m-%d'
    iso_format = '%Y-%m-%dT%H:%M:%S'

    def call_webservice(self, url, headers, postfields=None):
        logger.info(url)
        buffer = BytesIO() # buffer
        c = pycurl.Curl() # ouverture du navigateur
        c.setopt(c.URL, url) # définition de l'URL
        c.setopt(c.WRITEDATA, buffer) # définition du buffer
        c.setopt(c.HTTPHEADER, headers) # Ajoute l'entete d'autorisation avec la concatenation
        if postfields:
            c.setopt(c.POSTFIELDS, postfields) # ajoute les champs envoyer avec la method POST
        c.perform() # execute le navigateur
        response_code = c.getinfo(c.RESPONSE_CODE) # récupération du code de réponse http
        c.close() # fermeture du navigateur
        return json.loads(buffer.getvalue()), response_code

    def get_token(self):
        basic = '%s:%s' % (settings.INSEE_KEY, settings.INSEE_SECRET)
        basic = base64.b64encode(basic.encode('utf-8')).decode('utf-8')
        headers = ["Authorization: Basic %s" % basic]
        buffer, response_code = self.call_webservice(self.token_url, headers, "grant_type=client_credentials")
        try:
            return buffer["access_token"]
        except Exception:
            return False

    def get_companies(self, qreq, number=50, offset=0):
        message, companies, total, pages = (False, [], 0, 0)
        access_token = self.get_token()
        headers = ['Accept: application/json', 'Authorization: Bearer %s' % access_token]
        url = "%s?q=%s&nombre=%s&debut=%s&masquerValeursNulles=true" % (self.siret_url, qreq, number, offset)
        buffer, response_code = self.call_webservice(url, headers)
        message = buffer['header']['message']
        if str(response_code)[0] in ["2", "3"]:
            for company in buffer.get('etablissements', [buffer['header']]):
                companies.append({
                    'siren': company.get('siren'),
                    'siret': company.get('siret'),
                    'denomination': company['uniteLegale'].get('denominationUniteLegale', company['uniteLegale'].get('nomUniteLegale')),
                    'legalform': company['uniteLegale']['categorieJuridiqueUniteLegale'],
                    'ape': company['uniteLegale']['activitePrincipaleUniteLegale'].replace('.', ''),
                    'since': self.since(company['uniteLegale']['dateCreationUniteLegale']),
                    'address': {
                        'nic': company['nic'],
                        'street_number': company['adresseEtablissement'].get('numeroVoieEtablissement'),
                        'way': company['adresseEtablissement'].get('typeVoieEtablissement'),
                        'route': company['adresseEtablissement'].get('libelleVoieEtablissement'),
                        'locality': company['adresseEtablissement'].get('libelleCommuneEtablissement',
                            company['adresseEtablissement'].get('libelleCommuneEtrangerEtablissement')),
                        'postal_code': company['adresseEtablissement'].get('codeCommuneEtablissement', 
                            company['adresseEtablissement'].get('codePostalEtablissement')),
                        'country': company['adresseEtablissement'].get('libellePaysEtrangerEtablissement', 'france').lower(),
                        'country_code': company['adresseEtablissement'].get('codePaysEtrangerEtablissement', 'fr').lower(),
                        'cedex': company['adresseEtablissement'].get('libelleCedexEtablissement'),
                        'cedex_code': company['adresseEtablissement'].get('codeCedexEtablissement'),
                        'special': company['adresseEtablissement'].get('distributionSpecialeEtablissement'),
                        'complement': company['adresseEtablissement'].get('complementAdresseEtablissement'),
                        'index': company['adresseEtablissement'].get('indiceRepetitionEtablissement'),
                    }
                })
        return message, companies, total, pages

    def get_company_by_siren(self, siren):
        return self.get_companies('siren:%s' % siren)
        companies, total, pages = ([], 0, 0)
        if not siren.isdigit() or not len(siren) == 9:  return companies, total, pages
        access_token = self.get_token()
        headers = ['Accept: application/json', 'Authorization: Bearer %s' % access_token]
        buffer, response_code = self.call_webservice(self.siren_url, headers,  "q=siren:%s&masquerValeursNulles=true" % siren)
        for company in self.companies(buffer.get('unitesLegales', [buffer['header']]), response_code):
            companies.append({
                'siren': company.get('siren'),
                'denomination': company['periodesUniteLegale'][0]['denominationUniteLegale'],
                'category': company.get('categorieEntreprise'),
                'legalform_code': company['periodesUniteLegale'][0]['categorieJuridiqueUniteLegale'],
                'legalform_label': self.legalform(company['periodesUniteLegale'][0]['categorieJuridiqueUniteLegale']),
                'ape_code': company['periodesUniteLegale'][0]['activitePrincipaleUniteLegale'],
                'ape_label': self.ape(company['periodesUniteLegale'][0]['activitePrincipaleUniteLegale'].replace('.', '')),
                'street': '',
                'city': '',
                'since': self.createdate(company['dateCreationUniteLegale']),
                'lastupdate': self.lastupdate(company['dateDernierTraitementUniteLegale']),
            })
        return companies, total, pages

    def get_active_companies(self, number, offset):
        return self.get_companies('etatAdministratifUniteLegale:A', number, offset)

    def get_company_by_fulltext(self, fulltext):
        fulltext = re.sub(r"\s+", '-', fulltext)
        return self.get_companies('denominationUniteLegale:%s+AND+etatAdministratifUniteLegale:A' % fulltext)