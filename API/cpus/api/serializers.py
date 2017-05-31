from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from cpus.models import Cpu
from products.models import Product

class CpuSerializer(ModelSerializer):
    category = CharField(default='cpus', initial='cpus')
    class Meta:
        model = Cpu
        fields ='__all__'
