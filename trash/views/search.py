from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from mighty.views import TemplateView, FormView
from company.forms import CompanySearchByCountryForm
from company import backends_loop, translates as _, fields
from company.views.base import SearchByCountryBase

@method_decorator(login_required, name='dispatch')
class SearchByCountry(SearchByCountryBase, FormView):
    template_name = "company/country_search.html"
    form_class = CompanySearchByCountryForm
    success_url = '/company/search/'
    over_no_permission = True
    over_add_to_context = {'search': _.search, 'search_placeholder': _.search_placeholder, 'since': _.since}

@method_decorator(login_required, name='dispatch')
class APISearchByCountry(SearchByCountryBase, TemplateView):
    def get_context_data(self, **kwargs):
        if self.request.GET.get('search'):
            return self.get_results(self.request.GET.get('search'))
        return {}

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=True, **response_kwargs)

if 'rest_framework' in settings.INSTALLED_APPS:
    from rest_framework.views import APIView
    from rest_framework.response import Response

    class APISearchByCountry(SearchByCountryBase, APIView):
        def get_context_data(self, **kwargs):
            if self.request.GET.get('search'):
                return self.get_results(self.request.GET.get('search'))
            return {}

        def get(self, request, format=None):
            return Response(self.get_context_data())

