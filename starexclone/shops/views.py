from rest_framework.generics import ListAPIView
from .models import Shop
from.serializers import ShopSerilizer
from rest_framework.permissions import AllowAny


class ShopListApiView(ListAPIView):
    queryset=Shop.objects.all()
    serializer_class=ShopSerilizer
    permission_classes=[AllowAny]



class ShopByCategoryApiView(ListAPIView):
    serializer_class=ShopSerilizer


    def get_queryset(self):
        country=self.kwargs.get('country')
        return Shop.objects.filter(category=country)

