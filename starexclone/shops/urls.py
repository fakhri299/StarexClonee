from django.urls import path,include
from .views import ShopListApiView,ShopByCategoryApiView,CountryApi

urlpatterns = [
    path('',ShopListApiView.as_view()),
    path('<slug:slug>',ShopByCategoryApiView.as_view()),
    path('countries',CountryApi.as_view()),
]