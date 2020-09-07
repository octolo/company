from rest_framework.serializers import ModelSerializer
from company import get_company_model, fields

company_model = get_company_model()
companyfr_model = get_company_model('CompanyFR')

class CompanyFRSerializer(ModelSerializer):
    class Meta:
        model = companyfr_model
        fields = fields.fr

class CompanySerializer(ModelSerializer):
    class Meta:
        model = company_model
        fields = fields.company