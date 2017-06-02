from rest_framework.serializers import (
                        ModelSerializer,
                        SerializerMethodField,
                        CharField,
                        HyperlinkedModelSerializer,
                        ReadOnlyField,
                        IntegerField,
                        )

from orders.models import Order
from products.models import Product
from users.models import User
from products.api.serializers import ProductSerializer

# class OrderTotalSerializer(ModelSerializer):
#     orders_count  = SerializerMethodField()
#     # orders_count = IntegerField(source = 'products.count', read_only=True)
#     class Meta:
#         model = Order
#         fields = ('orders_count',)
#
#     def get_orders_count(self, obj):
#         return Order.objects.count()


class OrderSerializer(ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Order
        fields ='__all__'
        depth = 1

class OrderThroughSerializer(ModelSerializer):
    class Meta:
        model = Order.products.through
        fields = '__all__'
