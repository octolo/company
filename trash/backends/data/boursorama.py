from company.backends.data import CompanyDataBackend
from mighty.functions import similar_text
from lxml import html
import requests, re, json, time

class CompanyDataBackend(CompanyDataBackend):
    icb = {
        "Activités minières générales": "Matériaux de base",
        "Aérospatiale": "Industries",
        "Agences de médias": "Services aux consommateurs",
        "Agriculture et pêche": "Biens de consommation",
        "Ameublement": "Biens de consommation",
        "Assurance - Immobilière et dommages": "Sociétés Financières",
        "Assurance - Services complets": "Sociétés Financières",
        "Assurance vie": "Sociétés Financières",
        "Audiovisuel et divertissements": "Services aux consommateurs",
        "Automobiles": "Biens de consommation",
        "Banques": "Sociétés Financières",
        "Biens immobiliers destinés à la vente au détail": "Sociétés Financières",
        "Biotechnologie": "Santé",
        "Chemins de fer": "Industries",
        "Chimie de base": "Matériaux de base",
        "Chimie de spécialité": "Matériaux de base",
        "Compagnies aériennes": "Services aux consommateurs",
        "Composants et équipements électriques": "Technologies",
        "Construction lourde": "Industries",
        "Conteneurs et emballages": "Industries",
        "Courtiers en assurances": "Sociétés Financières",
        "Défense": "Industries",
        "Détaillants et grossistes - Alimentation": "Services aux consommateurs",
        "Distillateurs et viticulteurs": "Biens de consommation",
        "Distributeurs - Diversifiés": "Sociétés Financières",
        "Distributeurs - Habillement": "Biens de consommation",
        "Distributeurs spécialisés": "Sociétés Financières",
        "Distribution de gaz": "Services aux collectivités",
        "Eau": "Services aux collectivités",
        "Électricité alternative": "Services aux collectivités",
        "Électricité conventionnelle": "Services aux collectivités",
        "Électronique grand public": "Services aux collectivités",
        "Équipements de bureau électroniques": "Technologies",
        "Équipements de télécommunications": "Technologies",
        "Équipements électroniques": "Industries",
        "Équipements et services pétroliers": "Pétrole et gaz",
        "Équipements médicaux": "Santé",
        "Expert en finance": "Sociétés Financières",
        "Exploration et production": "Pétrole et gaz",
        "Fer et acier": "Matériaux de base",
        "Fournitures médicales": "Santé",
        "Gestion financière": "Sociétés Financières",
        "Gestionnaires d'actifs": "Sociétés Financières",
        "Habillement et accessoires": "Biens de consommation",
        "Hôtels": "Services aux consommateurs",
        "Industries diversifiées": "Industries",
        "Instruments de placement en actions": "Sociétés Financières",
        "Instruments de placement en titres nonparticipatifs": "Sociétés Financières",
        "Internet": "Technologies",
        "Jouets": "Biens de consommation",
        "Logiciels": "Technologies",
        "Materiaux et accessoires de construction": "Industries",
        "Matériel de production d'énergie renouvelable": "Pétrole et gaz",
        "Matériels informatiques": "Technologies",
        "Métaux non ferreux": "Matériaux de base",
        "Organismes de formation professionnelle et de placement": "Sociétés Financières",
        "Outillage industriel": "Industries",
        "Papiers": "Matériaux de base",
        "Participation et promotion immobilières": "Sociétés Financières",
        "Pharmacie": "Santé",
        "Pièces détachées d'automobiles": "Biens de consommation",
        "Pneus": "Biens de consommation",
        "Prestataires de soins de santé": "Santé",
        "Produits alimentaires": "Biens de consommation",
        "Produits de loisirs": "Biens de consommation",
        "Produits de soin personnel": "Biens de consommation",
        "Produits ménagers durables": "Biens de consommation",
        "Produits ménagers non durables": "Biens de consommation",
        "Réassurance": "Sociétés Financières",
        "Restaurants et bars": "Services aux consommateurs",
        "SCPI : biens immobiliers diversifiés": "Sociétés Financières",
        "SCPI : biens immobiliers industriels et bureautiques": "Sociétés Financières",
        "Semi-conducteurs": "Technologies",
        "Services d'appui professionnels": "Industries",
        "Services de livraison": "Industries",
        "Services de loisirs": "Services aux consommateurs",
        "Services de traitement et d'éliminationdes déchets": "Industries",
        "Services de transport": "Industries",
        "Services d'investissements": "Sociétés Financières",
        "Services informatiques": "Technologies",
        "Services multiples aux collectivités": "Services aux collectivités",
        "Sociétés pétrolières et gazières intégrées": "Pétrole et gaz",
        "Télécommunications filaires": "Télécommunications",
        "Véhicules commerciaux et camions": "Industries",
        "Voyage et tourisme": "Services aux consommateurs",
        "Construction individuelle": "Services aux consommateurs",
        "Édition": "Services aux consommateurs",
        "Jeux de hasard et d'argent": "Services aux consommateurs",
        "SCPI : biens immobiliers industriels et bureautiques": "Sociétés Financières",
        "Fer et acier": "Matériaux de base",
    }
    urls = {
        "search": "https://www.boursorama.com/recherche/",
        "home": "https://www.boursorama.com/cours/",
        "profil": "https://www.boursorama.com/cours/societe/profil/",
        "keysnumber": "https://www.boursorama.com/cours/societe/chiffres-cles/",
    }
    way_html = {
        "site": '//*[@id="main-content"]/div/section[1]/div[3]/div[1]/div/div/div[2]/div/ul/li[3]/p[2]/a',
        "icb1": '//*[@id="main-content"]/div/section/header/div/div/div[2]/div[2]/div/ul/li[1]/p[2]/a',
        "icb2": '//*[@id="main-content"]/div/section[1]/header/div/div/div[2]/div[2]/div/ul/li[1]/p[2]/a',
        "ticker": '//*[@id="main-content"]/div/section[1]/header/div/div/div[1]/div[2]/h2',
        "market": '//*[@id="main-content"]/div/section[1]/div[3]/div[1]/div/div/div[2]/div/ul/li[8]/p[2]',
        "capital_division": '//*[@id="main-content"]/div/section[1]/div[3]/div[2]/article/div[3]/div/div[2]/div[1]/div/script',
        "valorisation": '//*[@id="main-content"]/div/section[1]/div[3]/div[1]/div/div/div[2]/div/ul/li[7]/p[2]',
        "effective": '//*[@id="main-content"]/div/section/div[3]/div[1]/div/div/div[2]/div/ul/li[5]/p[2]',
        "current": '//*[@id="main-content"]/div/section/header/div/div/div[1]/div[1]/div/div[1]/span[1]',
        "securities": '//*[@id="main-content"]/div/section[1]/div[3]/div[1]/div/div/div[2]/div/ul/li[6]/p[2]',
        "dividend": '//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div/div[1]/div[12]/div[2]/div[1]/div/table/tbody',
        "net_profit": '//*[@id="main-content"]/div/section[1]/div[3]/div/article/div[1]/div/div[2]/div[1]/div/table/tbody',
        "turnover": '//*[@id="main-content"]/div/section[1]/div[3]/div/article/div[1]/div/div[2]/div[1]/div/table/tbody',
    }
    html_search = None
    html_home = None
    html_profil = None
    html_keysnumber = None

    lxml_search = None
    lxml_home = None
    lxml_profil = None
    lxml_keysnumber = None

    @property
    def choices_icb(self):
        return {
            "Matériaux de base": self.choices.MATERIALBASE,
            "Industries": self.choices.INDUSTRY,
            "Services aux consommateurs": self.choices.SERVICESCONS,
            "Biens de consommation": self.choices.GOODCONS,
            "Sociétés Financières": self.choices.COMPANYFINANCIAL,
            "Services aux collectivités": self.choices.SERVICESCOLLECT,
            "Santé": self.choices.HEALTH,
            "Technologies": self.choices.TECHNOLOGIES,
            "Pétrole et gaz": self.choices.PETROLGAS,
            "Télécommunications": self.choices.TELECOM,
        }

    @property
    def choices_market(self):
        choices = {m[1]: m[0] for m in self.choices.MARKET}
        return choices

    def prepare_boursorama_lxml(self):
        url_search = self.urls["search"]+self.obj.isin
        self.html_search = self.get_page(url_search)
        if self.html_search.url != url_search:
            redirect = re.search("/cours/.*/", self.html_search.url).group(0)
            self.html_home = self.get_page(redirect.replace("/cours/", self.urls["home"]))
            self.lxml_home = html.fromstring(self.html_home.content)
            self.html_profil = self.get_page(redirect.replace("/cours/", self.urls["profil"]))
            self.lxml_profil = html.fromstring(self.html_profil.content)
            self.html_keysnumber = self.get_page(redirect.replace("/cours/", self.urls["keysnumber"]))
            self.lxml_keysnumber = html.fromstring(self.html_keysnumber.content)
        else:
            self.backend_error("Can't init for %s" % self.obj)

    def try_to_prepare(self):
        try:
            self.prepare_boursorama_lxml()
        except requests.ConnectionError:
            self.logger.warning("Connection error waiting 60seconds")
            time.sleep(60)
            self.try_to_prepare()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.try_to_prepare()

    def get_page(self, url):
        return requests.get(url)
    def scrap_data(self, doc, path, raw=False):
        if raw: return doc.xpath(self.way_html[path])[0]
        return doc.xpath(self.way_html[path])[0].text_content().strip()

    def get_div_float(self):
        try:
            capital_division = self.scrap_data(self.lxml_profil, "capital_division").replace(' ', '')
            capital_division = re.findall(re.compile(r"JSON.parse\('(.+)'\)", re.MULTILINE), capital_division)
            capital_division = json.loads(capital_division[0])
            capital_division = capital_division['data']['amChartData']
            flottant = False
            total = 0
            ncapitaldivision = {}
            for cd in capital_division:
                if similar_text(cd["name"].lower(), "flottant") > 80:
                    flottant = cd["interest"]
                else:
                    ncapitaldivision[cd["name"]] = cd["interest"]
                    total += cd["interest"]
            if not flottant:
                flottant = 100-total
            ncapitaldivision["Flottant"] = flottant
            return ncapitaldivision, flottant
        except Exception as e:
            self.logger.warning("CapitalDivision/Float not found")

    @property
    def data_site(self):
        try:
            return self.scrap_data(self.lxml_profil, "site").replace(' ', '')
        except Exception as e:
            self.logger.warning("Site not found")

    @property
    def data_icb(self):
        try:
            icb = self.scrap_data(self.lxml_profil, "icb1")
            if not len(icb): icb = self.scrap_data(self.lxml_profil, "icb2")
            return self.choices_icb[self.icb[icb]]
        except Exception as e:
            self.logger.warning("Icb not found")

    def set_data_ticker(self, value):
        self.obj.ticker = value
    def get_data_ticker(self):
        return self.obj.ticker
    @property
    def data_ticker(self):
        try:
            ticker = self.scrap_data(self.lxml_profil, "ticker")
            return ticker.split(' ').pop()
        except Exception as e:
            self.logger.warning("Tiker not found")

    @property
    def data_market(self):
        try:
            market = self.scrap_data(self.lxml_profil, "market")
            return self.choices_market[market]
        except Exception as e:
            self.logger.warning("Market not found")

    # CAPITAL DIVISION
    @property
    def data_capital_division(self):
        try:
            capital_division, floatting = self.get_div_float()
            return capital_division
        except Exception as e:
            self.logger.warning("CapitalDivision not found")

    @property
    def data_floating(self):
        try:
            capital_division, floating = self.get_div_float()
            return floating
        except Exception as e:
            self.logger.warning("Floating not found")

    # CAPITALISATION
    @property
    def data_valorisation(self):
        try:
            captz = self.scrap_data(self.lxml_profil, "valorisation").split(" ")
            captz.pop()
            return float(''.join(captz))
        except Exception as e:
            self.logger.warning("Valorisation not found")

    # EFFECTIVE
    @property
    def data_effective(self):
        try:
            effective = self.scrap_data(self.lxml_profil, "effective").replace(' ', '')
            effective = re.findall("\d+", effective)[0]
            return int(effective)
        except Exception as e:
            self.logger.warning("Effective not found")

    # CURRENT
    @property
    def data_current(self):
        try:
            current = self.scrap_data(self.lxml_profil, "current").replace(' ', '')
            return float(current)
        except Exception as e:
            self.logger.warning("Current not found")

    # SECURITIES
    @property
    def data_securities(self):
        try:
            securities = self.scrap_data(self.lxml_profil, "securities").replace(' ', '')
            return int(securities)
        except Exception as e:
            self.logger.warning("Securities not found")

    @property
    def data_dividend(self):
        try:
            dividend = self.scrap_data(self.lxml_home, "dividend", True)
            for tr in dividend.xpath('.//tr'):
                if "Dividende" in tr[0].text_content():
                    dividend = tr[3].text_content().strip()
                    dividend = re.findall("\d+\.\d+", dividend)[0]
                    return float(dividend)
                    break
        except Exception as e:
            self.logger.warning("Dividend not found")

    @property
    def data_net_profit(self):
        try:
            net_profit = self.scrap_data(self.lxml_keysnumber, "net_profit", True)
            for tr in net_profit.xpath('.//tr'):
                if "Résultat net (part du groupe)" in tr[0].xpath('.//div')[0].text_content():
                    net_profit = tr[-1].xpath('.//div')[0].text_content().strip().replace(' ', '')
                    return int(net_profit)
                    break
        except Exception as e:
            self.logger.warning("Net profit not found")

    @property
    def data_turnover(self):
        try:
            turnover = self.scrap_data(self.lxml_keysnumber, "turnover", True)
            for tr in turnover.xpath('.//tr'):
                if "Chiffre d'affaires" in tr[0].xpath('.//div')[0].text_content():
                    turnover = tr[-1].xpath('.//div')[0].text_content().strip().replace(' ', '')
                    return int(turnover)*1000
                    break
        except Exception as e:
            self.logger.warning("turnover not found")
