from django.conf.urls import url
from django.contrib import admin

from .views import (
                    ProductList,
                    ProductCreate,
                    ProductDetail,
                    ProductUpdate,
                    ProductDestroy,
                    )

urlpatterns = [
    url(r'^$', ProductList.as_view(), name='list'),
    url(r'^create/$', ProductCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ProductDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', ProductUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', ProductDestroy.as_view(), name='delete'),
]
