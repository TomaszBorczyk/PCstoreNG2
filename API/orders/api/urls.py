from django.conf.urls import url
from django.contrib import admin
from .views import (
                    OrderList,
                    OrderCreate,
                    OrderDetail,
                    OrderDelete,
                    OrderUpdate,
                    OrderProductList,
                    OrderTotalList,
                    Bestsellers,
                    )

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', OrderList.as_view(), name='list'),
    url(r'^create/$', OrderCreate.as_view(), name='create'),
    url(r'^order-product/$', OrderProductList.as_view(), name='order_product'),
    url(r'^bestsellers/$', Bestsellers.as_view(), name='order_product'),
    url(r'^totals/$', OrderTotalList.as_view(), name='order_product'),
    url(r'^(?P<product_code>[\w-]+)/$', OrderDetail.as_view(), name='detail'),
    url(r'^(?P<product_code>[\w-]+)/delete/$', OrderDelete.as_view(), name='delete'),
    url(r'^(?P<product_code>[\w-]+)/update/$', OrderUpdate.as_view(), name='update'),
]
