from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from ssds.models import Ssd
from products.models import Product


class SsdSerializer(ModelSerializer):
    category = CharField(default='ssds', initial='ssds')
    class Meta:
        model = Ssd
        fields ='__all__'
