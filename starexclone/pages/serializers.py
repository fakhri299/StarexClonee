from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import SizeProduct

class SizeProductSerializer(ModelSerializer):
    
    class Meta:
        model=SizeProduct
        fields='__all__'


    def get_price(self,obj):
        if obj.country == 'TÜRKİYƏ':
            return obj.weight * 4
        
        elif obj.country == 'ÇİN':
            return obj.weight * 8

        elif obj.country == 'ABŞ':
            return obj.weight * 9

