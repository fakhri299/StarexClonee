from django.urls import path,include
from.views import *
from.views import *


urlpatterns = [
    path('countries',CountryApi.as_view()),
    path('<slug:country_slug>',ContactStorageApi.as_view()),
]
