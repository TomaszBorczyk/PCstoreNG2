from django.shortcuts import render
from rest_framework.generics import (
                                    ListAPIView,
                                    CreateAPIView,
                                    RetrieveAPIView,
                                    DestroyAPIView,
                                    UpdateAPIView,
                                    )
from ssds.models import Ssd
from .serializers import (
                        SsdSerializer,
                        )

# Create your views here.
class SsdList(ListAPIView):
    queryset=Ssd.objects.all()
    serializer_class = SsdSerializer

class SsdCreate(CreateAPIView):
    queryset = Ssd.objects.all()
    serializer_class = SsdSerializer

class SsdDetail(RetrieveAPIView):
    queryset = Ssd.objects.all()
    serializer_class = SsdSerializer
    lookup_field = 'product_code'

class SsdDelete(DestroyAPIView):
    queryset = Ssd.objects.all()
    serializer_class = SsdSerializer
    lookup_field = 'product_code'

class SsdUpdate(UpdateAPIView):
    queryset = Ssd.objects.all()
    serializer_class = SsdSerializer
    lookup_field = 'product_code'
