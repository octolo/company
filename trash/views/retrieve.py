from django.conf import settings
if 'rest_framework' in settings.INSTALLED_APPS:
    from rest_framework.generics import RetrieveAPIView
    from company import serializers
    from company import get_company_model

    class APICompanyDetail(RetrieveAPIView):
        queryset = get_company_model().objects.all()
        serializer_class = serializers.CompanySerializer
        lookup_field = 'uid'



            