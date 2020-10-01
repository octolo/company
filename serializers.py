from rest_framework.serializers import ModelSerializer
from company import get_company_model, fields
from mighty.decorators import maskedSerializer

except_mask = ('uid', 'denomination', 'capital_division', 'image_url')
company_model = get_company_model()
companyfr_model = get_company_model('CompanyFR')

base_fields = ('uid', 'denomination', 'image_url', 'since','site','effective','secretary','resume', 'infos', 'marketplace', 'rules')

@maskedSerializer(except_mask=except_mask)
class CompanyMinSerializer(ModelSerializer):
    class Meta:
        model = company_model
        fields = ('uid', 'denomination', 'image_url')

@maskedSerializer(except_mask=('uid', 'denomination'))
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

@maskedSerializer(except_mask=except_mask)
class CompanySerializer(ModelSerializer):
    class Meta:
        model = company_model
        fields = base_fields

@maskedSerializer(except_mask=except_mask)
class CompanyWithCountriesSerializer(ModelSerializer):
    siege_fr = CompanyFRSerializer(many=False)

    #def to_internal_value(self, data):
    #    print(data)
    #    return super().to_internal_value(data)

    #def to_representation(self, instance):
    #    ret = super().to_representation(instance)
    #    for field in ret:
    #        print('%s: %s' % (field, ret[field]))
    #    return ret
    #    #return 'test'

    class Meta:
        model = company_model
        fields = base_fields + ('siege_fr',)
