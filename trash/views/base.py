from django.conf import settings

from company import backends_loop, fields, get_company_model
from company import translates as _
from company.apps import CompanyConfig as conf
from company.forms import CompanyAddByCountry
from mighty.functions import get_form_model


class CanContainParentObject:
    country = 'fr'
    parent_object = None

    @property
    def company_model(self):
        return get_company_model()

    @property
    def country_model(self):
        return get_company_model(getattr(conf.Model, 'Company%s' % self.get_country().upper()))

    @property
    def country_fields(self):
        return fields.country + getattr(fields, self.get_country())[0:5]

    @property
    def country_form(self):
        return get_form_model(self.country_model, form_class=CompanyAddByCountry, form_fields=self.country_fields)

    def get_country(self):
        return self.kwargs.get('country', self.country)

    def get_country_form(self):
        return get_form_model(self.country_model, form_class=CompanyAddByCountry, form_fields=self.country_fields)

    def get_parent_object(self):
        if self.parent_object:
            return self.parent_object
        if self.kwargs.get('uid'):
            return self.company_model.objects.get(uid=self.kwargs.get('uid'))
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'fake': self.company_model()})
        parent_object_uid = context.get('object_id', self.kwargs.get('uid'))
        if not context.get('parent_object') and parent_object_uid:
            parent_object = self.company_model.objects.get(uid=parent_object_uid)
            context.update({'parent_object': parent_object})
        return context


class SearchByCountryBase(CanContainParentObject):
    def get_results(self, search):
        message, companies, total, pages = backends_loop(self.kwargs.get('country', 'fr'), search)
        return {
            'search': search,
            'object_list': companies,
            'message': message,
            'total': total,
            'pages': pages,
            'error': False,  # cf.message,
            'results': _.results % total if int(total) > 1 else _.result % total,
            'strpages': _.pages % pages if int(pages) > 1 else _.page % pages,
            'toomuch': _.toomuch % total,
        }

    def country_definition(self):
        country = self.get_country()
        return {
            'fake_country': self.country_model(),
            'country': country,
            'nationality': self.get_nationality(country),
            'country_fields': self.country_fields,
        }

    def get_nationality(self, country):
        if 'mighty.applications.nationality' in settings.INSTALLED_APPS:
            from mighty.models import Nationality
            nationality = Nationality.objects.get(alpha2__iexact=country)
            return nationality
        return country

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = self.get_country()
        context.update(self.country_definition())
        if self.request.GET.get('search'):
            context.update(self.get_results(self.request.GET.get('search')))
        return context
