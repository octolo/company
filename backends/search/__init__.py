from company.choices import fr as choices
from mighty.errors import BackendError
import datetime, logging
logger = logging.getLogger(__name__)

CHOICES_APE = dict(choices.APE)
CHOICES_LEGALFORM = dict(choices.LEGALFORM)
CHOICES_SLICE = dict(choices.SLICE_EFFECTIVE)

class SearchBackend:
    message = None
    since_format = None
    iso_format = '%Y-%m-%dT%H:%M:%S.%f%z'

    def in_error(self, message):
        self.message = message

    def backend_error(self, msg):
        raise BackendError(msg)

    def companies(self, companies, response_code):
        if str(response_code)[0] == '4': self.in_error(companies[0]['message'])
        elif str(response_code)[0] == '5': self.in_error('error server')
        return companies

    def get_ape_str(self, code):
        try:
            return CHOICES_APE[code]
        except Exception:
            pass
        return code

    def get_legalform_str(self, code):
        try:
            code = int(code)
            return CHOICES_LEGALFORM[code]
        except Exception:
            pass
        return code

    def get_slice_str(self, code):
        try:
            return CHOICES_SLICE[code]
        except Exception:
            pass
        return code

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