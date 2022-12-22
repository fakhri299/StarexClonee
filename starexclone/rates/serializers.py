from.models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class CountrySerializer(ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'



class CargoMethodSerializer(ModelSerializer):
    country=CountrySerializer()
    class Meta:
        model=CargoMethod 
        fields='__all__'


class RateSerializer(ModelSerializer):
    type=CargoMethodSerializer()
    class Meta:
        model=Rate
        fields='__all__'