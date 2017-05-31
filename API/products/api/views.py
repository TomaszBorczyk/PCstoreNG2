import functools, operator
from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import (
                                    ListAPIView,
                                    CreateAPIView,
                                    )
from products.models import Product
from .serializers import (
                        ProductSerializer,
                        )

# Create your views here.
class ProductList(ListAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None and search is not "":
            search_l = search.split()
            queryset = queryset.filter(functools.reduce(operator.or_, (Q(name__icontains=x) for x in search_l)))
        return queryset

class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
