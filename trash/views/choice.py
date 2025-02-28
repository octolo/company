from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from company.views.base import CanContainParentObject
from mighty.views import TemplateView


@method_decorator(login_required, name='dispatch')
class ChoiceCountry(CanContainParentObject, TemplateView):
    template_name = 'company/country_choice.html'

    def get_countries(self):
        alpha2 = [alpha2 for alpha2, backends in settings.COMPANY_BACKENDS.items()]
        if 'mighty.applications.nationality' in settings.INSTALLED_APPS:
            from mighty.models import Nationality
            nationalities = {nat[0].lower(): {'alpha2': nat[0].lower(), 'image': nat[1]} for nat in Nationality.objects.values_list('alpha2', 'image')}
            return [nationalities[al] if al in nationalities else {'alpha2': al.lower(), 'image': None} for al in alpha2]
        return [{'alpha2': al.lower(), 'image': None} for al in alpha2]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object_list': self.get_countries()})
        return context
