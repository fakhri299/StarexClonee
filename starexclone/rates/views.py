from rest_framework.generics import ListAPIView
from.serializers import *
from rest_framework.permissions import AllowAny



class RateApi(ListAPIView):
    serializer_class=RateSerializer

    def get_queryset(self):
        slug=self.kwargs.get('slug')
        return Rate.objects.filter(type__country__slug=slug)
       
