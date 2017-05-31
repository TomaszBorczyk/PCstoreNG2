from django.shortcuts import render
from rest_framework.generics import (
                                    ListAPIView,
                                    CreateAPIView,
                                    RetrieveAPIView,
                                    DestroyAPIView,
                                    UpdateAPIView,
                                    )
from cpus.models import Cpu
from .serializers import (
                        CpuSerializer,
                        )

# Create your views here.
class CpuList(ListAPIView):
    queryset=Cpu.objects.all()
    serializer_class = CpuSerializer

class CpuCreate(CreateAPIView):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

class CpuDetail(RetrieveAPIView):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer
    lookup_field = 'product_code'

class CpuDelete(DestroyAPIView):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer
    lookup_field = 'product_code'

class CpuUpdate(UpdateAPIView):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer
    lookup_field = 'product_code'
