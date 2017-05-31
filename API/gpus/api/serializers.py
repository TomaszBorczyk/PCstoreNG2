from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from gpus.models import Gpu
from products.models import Product


class GpuSerializer(ModelSerializer):
    category = CharField(default='gpus', initial='gpus')
    class Meta:
        model = Gpu
        fields ='__all__'
