from django.shortcuts import render
from rest_framework.generics import ListAPIView
from.serializers import *
from.models import *

# Create your views here.

class ContactStorageApi(ListAPIView):
    serializer_class=ContactSerializer


    def get_queryset(self):
        slug=self.kwargs.get('country_slug')
        return Contact.objects.filter(country__slug=slug)



class CountryApi(ListAPIView):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer
