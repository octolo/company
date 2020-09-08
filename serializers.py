from rest_framework.serializers import ModelSerializer
from company import get_company_model, fields

company_model = get_company_model()
companyfr_model = get_company_model('CompanyFR')

class CompanyMinSerializer(ModelSerializer):
    class Meta:
        model = company_model
        fields = ('uid', 'denomination')

class CompanyFRSerializer(ModelSerializer):
    class Meta:
        model = companyfr_model
        fields = fields.fr + (
            'siren',
            'ape_label',
            'legalform_label',
            'get_slice_effective_display',
            'get_evaluation_display',
        )

class CompanySerializer(ModelSerializer):
    class Meta:
        model = company_model
        fields = ('uid',) + fields.company

class CompanyWithCountriesSerializer(ModelSerializer):
    company_fr = CompanyFRSerializer(many=True)

    class Meta:
        model = company_model
        fields = ('uid', 'image_url') + fields.company + ('company_fr',)
