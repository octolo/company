from rest_framework.serializers import ModelSerializer

from company import fields, get_company_model
from company.apps import CompanyConfig
from mighty.applications.address import fields as address_fields
from mighty.decorators import maskedSerializer

company_model = get_company_model()
fr_model = get_company_model('CompanyFR')
addressfr_model = get_company_model('CompanyAddressFR')
except_mask = ('uid', 'denomination', 'capital_division', 'image_url')


@maskedSerializer(except_mask=('uid', 'denomination'))
class CompanyFRSerializer(ModelSerializer):
    class Meta:
        model = fr_model
        fields = (*fields.fr, 'siren', 'ape_label', 'legalform_label', 'siren', 'isin', 'index')


@maskedSerializer(except_mask=('uid',))
class CompanyAddressFRSerializer(ModelSerializer):
    class Meta:
        model = addressfr_model
        fields = (*address_fields, 'representation')


@maskedSerializer(except_mask=except_mask)
class CompanyMinSerializer(ModelSerializer):
    class Meta:
        model = company_model
        fields = ('uid', 'named_id', 'denomination', 'image_url', 'siren', 'isin', 'index')


class CompanySerializer(ModelSerializer):
    siege_fr = CompanyFRSerializer(many=False)

    class Meta:
        model = company_model
        fields = fields.serializer + CompanyConfig.sz_fields + ('siren', 'isin', 'index')


@maskedSerializer(except_mask=except_mask)
class CompanyWithAddrFRSerializer(ModelSerializer):
    siege_fr = CompanyFRSerializer(many=False)
    companyfr_address = CompanyAddressFRSerializer(many=True, read_only=True)

    class Meta:
        model = company_model
        fields = fields.serializer + CompanyConfig.sz_fields + ('siren', 'isin', 'index', 'companyfr_address')
