from rest_framework.serializers import ModelSerializer, RelatedField, PrimaryKeyRelatedField, HyperlinkedModelSerializer
from products.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
