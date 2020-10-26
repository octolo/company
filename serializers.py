from rest_framework.serializers import ModelSerializer
from company import get_company_model, fields
from mighty.decorators import maskedSerializer

company_model = get_company_model()
companyfr_model = get_company_model('CompanyFR')
except_mask = ('uid', 'denomination', 'capital_division', 'image_url')


@maskedSerializer(except_mask=('uid', 'denomination'))
class CompanyFRSerializer(ModelSerializer):
    class Meta:
        model = companyfr_model
        fields = fields.fr + ('siren', 'ape_label', 'legalform_label')

@maskedSerializer(except_mask=except_mask)
class CompanyMinSerializer(ModelSerializer):
    class Meta:
        model = company_model
        fields = ('uid', 'denomination', 'image_url')

@maskedSerializer(except_mask=except_mask)
class CompanySerializer(ModelSerializer):
    siege_fr = CompanyFRSerializer(many=False)

    class Meta:
        model = company_model
        fields = fields.serializer
