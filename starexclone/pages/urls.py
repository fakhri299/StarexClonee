from django.urls import path,include
from .views import SizeApiView

urlpatterns = [
    path('',SizeApiView.as_view())
]