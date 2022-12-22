from django.urls import path,include
from.views import *


urlpatterns = [
    path('<slug:slug>',RateApi.as_view())
]
