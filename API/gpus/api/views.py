from django.shortcuts import render
from rest_framework.generics import (
                                    ListAPIView,
                                    CreateAPIView,
                                    RetrieveAPIView,
                                    DestroyAPIView,
                                    UpdateAPIView,
                                    )
from gpus.models import Gpu
from .serializers import (
                        GpuSerializer,
                        )

# Create your views here.
class GpuList(ListAPIView):
    queryset=Gpu.objects.all()
    serializer_class = GpuSerializer

class GpuCreate(CreateAPIView):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer

class GpuDetail(RetrieveAPIView):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer
    lookup_field = 'product_code'

class GpuDelete(DestroyAPIView):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer
    lookup_field = 'product_code'

class GpuUpdate(UpdateAPIView):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer
    lookup_field = 'product_code'
