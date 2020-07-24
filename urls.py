from django.urls import path, include
from company import views

#app_name = "company"
#urlpatterns = [
#    path('search/', views.CompanySearchFormView.as_view(), name="company-search"),
#    path('<str:siren>/', views.CompanyDetailView.as_view(), name='company-detail'),
#]

app_name=views.get_company_model()().app_label
urlpatterns = [path('', include(views.CompanyViewSet().urls)),]
