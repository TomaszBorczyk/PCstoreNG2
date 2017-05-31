from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from hdds.models import Hdd
from products.models import Product



class HddSerializer(ModelSerializer):
    category = CharField(default='hdds', initial='hdds')
    class Meta:
        model = Hdd
        fields ='__all__'
