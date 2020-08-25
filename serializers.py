from django.conf import settings
from rest_framework.serializers import ModelSerializer
from company import fields

class CompanySerializer(ModelSerializer):
    class Meta:
        fields = ('uid',) + fields.company