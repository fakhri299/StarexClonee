from django.urls import path,include
from .views import SizeApiView

urlpatterns = [
    path('details',SizeApiView.as_view())
]