from rest_framework.serializers import ModelSerializer

from mighty.decorators import maskedSerializer
from mighty.applications.address import fields as address_fields
from company import get_company_model, fields
from company.apps import CompanyConfig
from easyshares.models import Role

company_model = get_company_model()
fr_model = get_company_model('CompanyFR')
addressfr_model = get_company_model('CompanyAddressFR')
except_mask = ('uid', 'denomination', 'capital_division', 'image_url')


@maskedSerializer(except_mask=('uid', 'denomination'))
class CompanyFRSerializer(ModelSerializer):
    class Meta:
        model = fr_model
        fields = fields.fr + ('siren', 'ape_label', 'legalform_label')

@maskedSerializer(except_mask=('uid',))
class CompanyAddressFRSerializer(ModelSerializer):
    class Meta:
        model = addressfr_model
        fields = address_fields + ('representation',)

@maskedSerializer(except_mask=except_mask)
class CompanyMinSerializer(ModelSerializer):
    class Meta:
        model = company_model
        fields = ('uid', 'denomination', 'image_url')

@maskedSerializer(except_mask=except_mask)

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ('uid', 'name')

" Je l'ai mis la, ca fonctionnais pas dans quand c'est directement dans le serializer de easyshares "
class CompanySerializer(ModelSerializer):
    siege_fr = CompanyFRSerializer(many=False)
    roles = RoleSerializer(many=True, source="group_role")

    class Meta:
        model = company_model
        fields = fields.serializer + CompanyConfig.sz_fields + ('roles', )

@maskedSerializer(except_mask=except_mask)
class CompanyWithAddrFRSerializer(ModelSerializer):
    siege_fr = CompanyFRSerializer(many=False)
    companyfr_address = CompanyAddressFRSerializer(many=True)

    class Meta:
        model = company_model
        fields = fields.serializer + CompanyConfig.sz_fields
