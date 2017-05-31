from django.shortcuts import render
from rest_framework.generics import (
                                    ListAPIView,
                                    CreateAPIView,
                                    RetrieveAPIView,
                                    DestroyAPIView,
                                    UpdateAPIView,
                                    )
from hdds.models import Hdd
from .serializers import (
                        HddSerializer,
                        )

# Create your views here.
class HddList(ListAPIView):
    queryset=Hdd.objects.all()
    serializer_class = HddSerializer

class HddCreate(CreateAPIView):
    queryset = Hdd.objects.all()
    serializer_class = HddSerializer

class HddDetail(RetrieveAPIView):
    queryset = Hdd.objects.all()
    serializer_class = HddSerializer
    lookup_field = 'product_code'

class HddDelete(DestroyAPIView):
    queryset = Hdd.objects.all()
    serializer_class = HddSerializer
    lookup_field = 'product_code'

class HddUpdate(UpdateAPIView):
    queryset = Hdd.objects.all()
    serializer_class = HddSerializer
    lookup_field = 'product_code'
