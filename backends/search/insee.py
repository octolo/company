from django.conf import settings
from company.backends.search import SearchBackend
from io import BytesIO
import base64, pycurl, json, re, logging, time, datetime
from mighty.functions import make_searchable
logger = logging.getLogger(__name__)

class SearchBackend(SearchBackend):
    token_url = 'https://api.insee.fr/token'
    siren_url = 'https://api.insee.fr/entreprises/sirene/V3/siren'
    siret_url = 'https://api.insee.fr/entreprises/sirene/V3/siret'
    since_format = '%Y-%m-%d'
    iso_format = '%Y-%m-%dT%H:%M:%S'
    error = 5

    def call_webservice(self, url, headers, postfields=None):
        buffer = BytesIO() # buffer
        c = pycurl.Curl() # ouverture du navigateur
        c.setopt(c.URL, url) # définition de l'URL
        c.setopt(c.WRITEDATA, buffer) # définition du buffer
        c.setopt(c.HTTPHEADER, headers) # Ajoute l'entete d'autorisation avec la concatenation
        if postfields:
            c.setopt(c.POSTFIELDS, postfields) # ajoute les champs envoyer avec la method POST
        try:
            c.perform() # execute le navigateur
            response_code = c.getinfo(c.RESPONSE_CODE) # récupération du code de réponse http
            c.close() # fermeture du navigateur
            datas = json.loads(buffer.getvalue())
        except Exception as e:
            logger.error(buffer.getvalue())
            logger.error(e)
            self.error-=1
            if self.error:
                return self.call_webservice(url, headers, postfields)
            else:
                raise e
        return datas, response_code

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
        if'header' in buffer:
            message = False if buffer['header']['message'] == "OK" else buffer['header']['message']
            total = buffer['header'].get('total', 0)
            pages = round(total/number) if total else 0
            if str(response_code)[0] in ["2", "3"]:
                for company in buffer.get('etablissements', [buffer['header']]):
                    companies.append({
                        'siret': company.get('siret'),
                        'denomination': company['uniteLegale'].get('denominationUniteLegale', company['uniteLegale'].get('nomUniteLegale')),
                        'legalform': company['uniteLegale']['categorieJuridiqueUniteLegale'],
                        'ape': company['uniteLegale']['activitePrincipaleUniteLegale'].replace('.', ''),
                        'ape_noun': company['uniteLegale']['nomenclatureActivitePrincipaleUniteLegale'],
                        'since': self.since(company['uniteLegale'].get('dateCreationUniteLegale')),
                        'category': company['uniteLegale'].get('categorieEntreprise', ''),
                        'slice_effective': company['uniteLegale'].get('trancheEffectifsUniteLegale', ''),
                        'siege':company.get('etablissementSiege', False),
                        'address': {
                            'address': ' '.join(filter(None, [
                                company['adresseEtablissement'].get('numeroVoieEtablissement'),
                                company['adresseEtablissement'].get('typeVoieEtablissement'),
                                company['adresseEtablissement'].get('libelleVoieEtablissement')
                            ])),
                            'complement': company['adresseEtablissement'].get('complementAdresseEtablissement', ''),
                            'locality': company['adresseEtablissement'].get('libelleCommuneEtablissement',
                                company['adresseEtablissement'].get('libelleCommuneEtrangerEtablissement', '')),
                            'postal_code': company['adresseEtablissement'].get('codePostalEtablissement', 
                                company['adresseEtablissement'].get('codeCommuneEtablissement', '')),
                            'country': company['adresseEtablissement'].get('libellePaysEtrangerEtablissement', 'france').lower(),
                            'country_code': company['adresseEtablissement'].get('codePaysEtrangerEtablissement', 'fr').lower(),
                            'cedex': company['adresseEtablissement'].get('libelleCedexEtablissement', ''),
                            'cedex_code': company['adresseEtablissement'].get('codeCedexEtablissement', ''),
                            'special': company['adresseEtablissement'].get('distributionSpecialeEtablissement', ''),
                            'index': company['adresseEtablissement'].get('indiceRepetitionEtablissement', ''),
                            'nic': company.get('nic')
                        }
                    })
            return message, companies, total, pages
        else:
            if 'fault' in buffer:
                if buffer['fault']['code'] == 900804:
                    sleepfor = 61-datetime.datetime.now().second
                    i = 0
                    while i < sleepfor:
                        logger.info("desc: %s, wait: %s seconds" % (buffer['fault']['description'], sleepfor))
                        time.sleep(1)
                        sleepfor-=1
                    return self.get_companies(qreq, number, offset)
                else:
                    logger.info(buffer)
            else:
                logger.info("Error encountered but we dont know what")

    def get_company_by_siren(self, siren):
        return self.get_companies('siren:%s+AND+etablissementSiege:true' % siren)

    def get_active_companies(self, number, offset):
        return self.get_companies('etatAdministratifUniteLegale:A', number, offset)

    def get_company_by_fulltext(self, fulltext):
        fulltext = re.sub(r"\s+", '-', fulltext)
        return self.get_companies('denominationUniteLegale:%s+AND+etatAdministratifUniteLegale:A' % make_searchable(fulltext))