from company.choices import fr as choices
import datetime

CHOICES_APE = dict(choices.APE)
CHOICES_LEGALFORM = dict(choices.LEGALFORM)

class SearchBackend:
    message = None
    since_format = None
    iso_format = '%Y-%m-%dT%H:%M:%S.%f%z'

    def in_error(self, message):
        self.message = message

    def companies(self, companies, response_code):
        if str(response_code)[0] == '4': self.in_error(companies[0]['message'])
        elif str(response_code)[0] == '5': self.in_error('error server')
        return companies

    def ape(self, code):
        return code#CHOICES_APE[code]

    def legalform(self, code):
        return int(code)#CHOICES_LEGALFORM[int(code)]

    def lastupdate(self, date):
        return datetime.datetime.strptime(date, self.iso_format).strftime("%Y-%m-%d")

    def since(self, date):
        return datetime.datetime.strptime(date, self.since_format).strftime("%Y-%m-%d")

    def get_companies(self, companies, response_code):
        raise NotImplementedError("Subclasses should implement get_companies()")

    def get_company_by_siren(self, siren):
        raise NotImplementedError("Subclasses should implement get_company_by_siren()")

    def get_company_by_fulltext(self, fulltext):
        raise NotImplementedError("Subclasses should implement get_company_by_fulltext()")

    def get_active_companies(self, fulltext):
        raise NotImplementedError("Subclasses should implement get_active_companies()")