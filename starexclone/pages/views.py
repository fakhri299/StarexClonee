from rest_framework.generics import ListCreateAPIView
from .models import SizeProduct
from .serializers import SizeProductSerializer


class SizeApiView(ListCreateAPIView):
    queryset=SizeProduct.objects.all()
    serializer_class=SizeProductSerializer


    



