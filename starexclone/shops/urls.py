from django.urls import path,include
from .views import ShopListApiView,ShopByCategoryApiView

urlpatterns = [
    path('shops',ShopListApiView.as_view()),
    path('shops/<str:country>',ShopByCategoryApiView.as_view()),
]