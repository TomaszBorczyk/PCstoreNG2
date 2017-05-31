from django.shortcuts import render
from rest_framework.generics import (
                                    ListAPIView,
                                    CreateAPIView,
                                    RetrieveAPIView,
                                    DestroyAPIView,
                                    UpdateAPIView,
                                    )
from rams.models import Ram
from .serializers import (
                        RamSerializer,
                        )

# Create your views here.
class RamList(ListAPIView):
    queryset=Ram.objects.all()
    serializer_class = RamSerializer

class RamCreate(CreateAPIView):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer

class RamDetail(RetrieveAPIView):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer
    lookup_field = 'product_code'

class RamDelete(DestroyAPIView):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer
    lookup_field = 'product_code'

class RamUpdate(UpdateAPIView):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer
    lookup_field = 'product_code'
