from core.management.commands.UpdateModel import UpdateModel
from core.functions import similar_text
from io import BytesIO
import re

from boarddata.models.company import CompanyAGData
from boarddata.models.assembly import Assembly
from boarddata.applications.company import translates as _
from boarddata.applications.company.models import (
    ICB_MATERIALBASE,
    ICB_INDUSTRY,
    ICB_SERVICESCONS,
    ICB_GOODCONS,
    ICB_COMPANYFINANCIAL,
    ICB_SERVICESCOLLECT,
    ICB_HEALTH,
    ICB_TECHNOLOGIES,
    ICB_PETROLGAS,
    ICB_TELECOM,
    MARKET_COMPA,
    MARKET_COMPB,
    MARKET_COMPC,
    MARKET_EURONEXT_Growth,
    MARKET_EURONEXT_Access,
    MARKET_OTHERS,
    MARKET_EXCEPT,
    MARKET_COMPASPECIAL,
    MARKET_DELISTED)

class Command(UpdateModel):
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    headers = {}
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
    choices_icb = {
        "Matériaux de base": ICB_MATERIALBASE,
        "Industries": ICB_INDUSTRY,
        "Services aux consommateurs": ICB_SERVICESCONS,
        "Biens de consommation": ICB_GOODCONS,
        "Sociétés Financières": ICB_COMPANYFINANCIAL,
        "Services aux collectivités": ICB_SERVICESCOLLECT,
        "Santé": ICB_HEALTH,
        "Technologies": ICB_TECHNOLOGIES,
        "Pétrole et gaz": ICB_PETROLGAS,
        "Télécommunications": ICB_TELECOM,
    }
    choices_market = {
        _.MARKET_COMPA: MARKET_COMPA,
        _.MARKET_COMPB: MARKET_COMPB,
        _.MARKET_COMPC: MARKET_COMPC,
        _.MARKET_EURONEXT_Growth: MARKET_EURONEXT_Growth,
        _.MARKET_EURONEXT_Access: MARKET_EURONEXT_Access,
        _.MARKET_OTHERS: MARKET_OTHERS,
        _.MARKET_EXCEPT: MARKET_EXCEPT,
        _.MARKET_COMPASPECIAL: MARKET_COMPASPECIAL,
        _.MARKET_DELISTED: MARKET_DELISTED,
    }

    def get_valorisation(self, document, obj):
        try:
            valorisation = document.xpath('//*[@id="main-content"]/div/section[1]/header/div/div/div[3]/div[2]/div/ul/li[2]/p[2]')
            valorisation = valorisation[0].text_content().strip().split(' ')
            valorisation.pop()
            valorisation = ''.join(valorisation)
            return float(valorisation)
        except Exception as e:
            self.error.add("Valorisation not found", obj, self.current_row)
        return obj.valorisation

    def get_effective(self, document, obj):
        try:
            effective = document.xpath('//*[@id="main-content"]/div/section/div[3]/div[1]/div/div/div[2]/div/ul/li[5]/p[2]')
            effective = effective[0].text_content().strip().replace(' ', '')
            effective = re.findall("\d+", effective)[0]
            return int(effective)
        except Exception as e:
            self.error.add("Effective not found", obj, self.current_row)
        return obj.effective

    def get_current(self, document, obj):
        try:
            current = document.xpath('//*[@id="main-content"]/div/section/header/div/div/div[1]/div[1]/div/div[1]/span[1]')
            current = current[0].text_content().strip().replace(' ', '')
            return float(current)
        except Exception as e:
            self.error.add("Current not found", obj, self.current_row)
        return obj.current

    def get_icb(self, document, obj):
        try:
            icb = document.xpath('//*[@id="main-content"]/div/section/header/div/div/div[2]/div[2]/div/ul/li[1]/p[2]/a')
            if not len(icb):
                icb = document.xpath('//*[@id="main-content"]/div/section[1]/header/div/div/div[2]/div[2]/div/ul/li[1]/p[2]/a')
            icb = icb[0].text_content().strip()
            return self.choices_icb[self.icb[icb]]
        except Exception as e:
            self.error.add("Icb not found", "%s: %s" % (obj, icb), self.current_row)
        return obj.icb

    def get_ticker(self, document, obj):
        try:
            ticker = document.xpath('//*[@id="main-content"]/div/section[1]/header/div/div/div[1]/div[2]/h2')
            ticker = ticker[0].text_content().strip()
            return ticker.split(' ').pop()
        except Exception as e:
            self.error.add("Ticker not found", obj, self.current_row)
        return obj.ticker

    def get_capital_division(self, document, obj):
        import json
        try:
            capital_division = document.xpath('//*[@id="main-content"]/div/section[1]/div[3]/div[2]/article/div[3]/div/div[2]/div[1]/div/script')
            capital_division = capital_division[0].text_content().strip().replace(' ', '')
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
            self.error.add("Capital division not found", obj, self.current_row)
        return obj.capital_division

    def get_site(self, document, obj):
        try:
            site = document.xpath('//*[@id="main-content"]/div/section[1]/div[3]/div[1]/div/div/div[2]/div/ul/li[3]/p[2]/a')
            site = site[0].text_content().strip().replace(' ', '')
            return site
        except Exception as e:
            self.error.add("Site not found", obj, self.current_row)
        return obj.site

    def get_market(self, document, obj):
        try:
            market = document.xpath('//*[@id="main-content"]/div/section[1]/div[3]/div[1]/div/div/div[2]/div/ul/li[8]/p[2]')
            market = market[0].text_content().strip()
            return self.choices_market[market]
        except Exception as e:
            self.error.add("Market not found", obj, self.current_row)
        return obj.market

    def get_securities(self, document, obj):
        try:
            securities = document.xpath('//*[@id="main-content"]/div/section[1]/div[3]/div[1]/div/div/div[2]/div/ul/li[6]/p[2]')
            securities = securities[0].text_content().strip().replace(' ', '')
            return int(securities)
        except Exception as e:
            self.error.add("Securities not found", obj, self.current_row)
        return obj.securities

    def get_dividend(self, document, obj):
        try:
            dividend = document.xpath('//*[@id="main-content"]/div/section[1]/div[2]/article/div[1]/div/div[1]/div[12]/div[2]/div[1]/div/table/tbody')[0]
            for tr in dividend.xpath('.//tr'):
                if "Dividende" in tr[0].text_content():
                    dividend = tr[3].text_content().strip()
                    dividend = re.findall("\d+\.\d+", dividend)[0]
                    return float(dividend)
                    break
        except Exception as e:
            self.error.add("Dividend not found", obj, self.current_row)
        return obj.dividend

    def get_net_profit(self, document, obj):
        try:
            net_profit = document.xpath('//*[@id="main-content"]/div/section[1]/div[3]/div/article/div[1]/div/div[2]/div[1]/div/table/tbody')[0]
            for tr in net_profit.xpath('.//tr'):
                if "Résultat net (part du groupe)" in tr[0].xpath('.//div')[0].text_content():
                    net_profit = tr[-1].xpath('.//div')[0].text_content().strip().replace(' ', '')
                    return int(net_profit)
                    break
        except Exception as e:
            self.error.add("Net profit not found", obj, self.current_row)
        return obj.net_profit

    def get_turnover(self, document, obj):
        try:
            turnover = document.xpath('//*[@id="main-content"]/div/section[1]/div[3]/div/article/div[1]/div/div[2]/div[1]/div/table/tbody')[0]
            for tr in turnover.xpath('.//tr'):
                if "Chiffre d'affaires" in tr[0].xpath('.//div')[0].text_content():
                    turnover = tr[-1].xpath('.//div')[0].text_content().strip().replace(' ', '')
                    return int(turnover)
                    break
        except Exception as e:
            self.error.add("Net profit not found", obj, self.current_row)
        return obj.turnover

    def do_update(self, obj):
        home = self.getWebPage('https://www.boursorama.com/recherche/%s' % obj.isin)
        if 'location' in self.headers:
            default = self.headers['location']
            home = self.getWebPage(default.replace('/cours/', 'https://www.boursorama.com/cours/'))
            profil = self.getWebPage(default.replace('/cours/', 'https://www.boursorama.com/cours/societe/profil/'))
            keysnumber = self.getWebPage(default.replace('/cours/', 'https://www.boursorama.com/cours/societe/chiffres-cles/'))
            obj.site = self.get_site(profil, obj)
            obj.icb = self.get_icb(profil, obj)
            obj.ticker = self.get_ticker(profil, obj)
            obj.market = self.get_market(profil, obj)
            obj.save()
            # AG DATA
            agdataobj = CompanyAGData.objects.filter(company=obj, assembly__date_assembly__year=2020).order_by('assembly__date_assembly').last()
            if not agdataobj:
                try:
                    assembly = Assembly.objects.filter(company=obj, date_assembly__year=2020).order_by('date_assembly').last()
                except Assembly.DoesNotExist:
                    assembly = Assembly(company=obj, date_assembly="2020-12-31")
                    assembly.save()
                agdataobj = CompanyAGData(company=obj, assembly=assembly)
                agdataobj.save()
            agdataobj.capital_division, agdataobj.floating = self.get_capital_division(profil, agdataobj)
            print("agdataobj.capital_division: %s" % agdataobj.capital_division)
            agdataobj.valorisation = self.get_valorisation(profil, agdataobj)
            print("agdataobj.valorisation: %s" % agdataobj.valorisation)
            agdataobj.effective = self.get_effective(profil, agdataobj)
            print("agdataobj.effective: %s" % agdataobj.effective)
            agdataobj.current = self.get_current(profil, agdataobj)
            print("agdataobj.current: %s" % agdataobj.current)
            agdataobj.securities = self.get_securities(profil, agdataobj)
            print("agdataobj.securities: %s" % agdataobj.securities)
            agdataobj.dividend = self.get_dividend(home, agdataobj)
            print("agdataobj.dividend: %s" % agdataobj.dividend)
            agdataobj.net_profit = self.get_net_profit(keysnumber, agdataobj)
            print("agdataobj.net_profit: %s" % agdataobj.net_profit)
            agdataobj.turnover = self.get_turnover(keysnumber, agdataobj)
            print("agdataobj.turnover: %s" % agdataobj.turnover)
            agdataobj.save()
