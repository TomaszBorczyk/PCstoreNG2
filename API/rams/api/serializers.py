from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from rams.models import Ram
from products.models import Product



class RamSerializer(ModelSerializer):
    category = CharField(default='rams', initial='Rams')
    class Meta:
        model = Ram
        fields ='__all__'
