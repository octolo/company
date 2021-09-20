from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from mighty.views import TemplateView, FormView
from company import create_company
from company.views.base import SearchByCountryBase, CanContainParentObject

@method_decorator(login_required, name='dispatch')
class AddByCountry(CanContainParentObject, FormView):
    template_name = 'company/countries/add.html'
    admin = False

    def get_form_class(self):
        return self.get_country_form()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            "country_model": self.get_country_model(),
            "country_fields": self.get_country_fields(),
            "parent_object": self.get_parent_object(),
            "admin": self.admin,
        })
        return kwargs

    def form_valid(self, form):
        form.save()
        self.success_url = form.new_company.admin_change_url if self.admin else form.new_company.detail_url
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AddBySiren(SearchByCountryBase, TemplateView):
    def get_context_data(self, **kwargs):
        if self.request.GET.get('siren'):
            results = self.get_results(self.request.GET.get('siren'))
            if len(results['object_list']) == 1:
                data, company = create_company('FR', results['object_list'][0])
                return data
        return {}

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=True, **response_kwargs)

@method_decorator(login_required, name='dispatch')
class AddByRna(SearchByCountryBase, TemplateView):
    def get_context_data(self, **kwargs):
        if self.request.GET.get('rna'):
            results = self.get_results(self.request.GET.get('rna'))
            if len(results['object_list']) == 1:
                data, company = create_company('FR', results['object_list'][0])
                return data
        return {}

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=True, **response_kwargs)


if 'rest_framework' in settings.INSTALLED_APPS:
    from rest_framework.views import APIView
    from rest_framework.response import Response

    class AddBySiren(SearchByCountryBase, APIView):
        def get_context_data(self, **kwargs):
            if self.request.GET.get('siren'):
                results = self.get_results(self.request.GET.get('siren'))
                if len(results['object_list']) == 1:
                    data, company = create_company('FR', results['object_list'][0])
                    return data
            return {}

        def get(self, request, format=None):
            return Response(self.get_context_data())

    class AddByRna(SearchByCountryBase, APIView):
        def get_context_data(self, **kwargs):
            if self.request.GET.get('rna'):
                results = self.get_results(self.request.GET.get('rna'))
                if len(results['object_list']) == 1:
                    data, company = create_company('FR', results['object_list'][0])
                    return data
            return {}

        def get(self, request, format=None):
            return Response(self.get_context_data())