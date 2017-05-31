from django.shortcuts import render
from django.db.models import Count, Avg
from rest_framework.generics import (
                                    ListAPIView,
                                    CreateAPIView,
                                    RetrieveAPIView,
                                    DestroyAPIView,
                                    UpdateAPIView,
                                    )
from orders.models import Order
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import (
                        OrderSerializer,
                        OrderThroughSerializer,
                        # OrderTotalSerializer,
                        )
from products.api.serializers import ProductSerializer



# class OrderTotalList(ListAPIView):
#     queryset = Order.objects.all()
    # serializer_class = OrderTotalSerializer

class Bestsellers(APIView):
    renderer_classes = (JSONRenderer,)
    # serializer_class = ProductSerializer

    def get(self, request, format=None):
    # def get_queryset(self):
        top = Order.products.through.objects.values('product_id').annotate(total=Count('product_id')).order_by('total')[:10]
        content = {'top': top, }
        return Response(content)



class OrderTotalList(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        orders_count = Order.objects.count()
        prd = Order.objects.annotate(num=Count('products'))
        avg_products=0
        for p in prd:
            avg_products += p.num
        avg_products /=orders_count
        content = {'orders_count': orders_count, 'avg_products':avg_products}
        return Response(content)


class OrderProductList(ListAPIView):
    # queryset = OrderProduct.objects.all()
    queryset = Order.products.through.objects.all()
    serializer_class = OrderThroughSerializer

class OrderList(ListAPIView):
    queryset=Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'product_code'

class OrderDelete(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'product_code'

class OrderUpdate(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'product_code'
