from .models import Shop
from rest_framework.serializers import ModelSerializer

class ShopSerilizer(ModelSerializer):
    class Meta:
        model=Shop
        fields='__all__'