from django.conf import settings

if 'rest_framework' in settings.INSTALLED_APPS:
    from rest_framework.generics import ListAPIView

    from company import filters, get_company_model, serializers
    from mighty.filters import FiltersManager, Foxid

    class APICompanyList(ListAPIView):
        queryset = get_company_model().objectsB.all()
        serializer_class = serializers.CompanySerializer
        lookup_field = 'uid'
        filters = filters.filters_list
        cache_manager = None

        @property
        def foxid(self):
            return Foxid(self.queryset, self.request, f=self.manager.flts).ready()

        @property
        def manager(self):
            if not self.cache_manager:
                self.cache_manager = FiltersManager(flts=self.filters)
            return self.cache_manager

        def get_queryset(self, queryset=None):
            return self.foxid.filter(*self.manager.params(self.request))
