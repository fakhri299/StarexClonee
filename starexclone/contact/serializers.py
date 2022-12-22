from.models import *
from rest_framework.serializers import ModelSerializer


class CountrySerializer(ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'


class ContactSerializer(ModelSerializer):
    country=CountrySerializer()
    class Meta:
        model=Contact
        fields='__all__'





