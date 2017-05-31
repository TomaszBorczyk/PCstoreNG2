from django.conf.urls import url
from django.contrib import admin
from .views import (
                    SsdList,
                    SsdCreate,
                    SsdDetail,
                    SsdDelete,
                    SsdUpdate,
                    )

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', SsdList.as_view(), name='list'),
    url(r'^create/$', SsdCreate.as_view(), name='create'),
    url(r'^(?P<product_code>[\w-]+)/$', SsdDetail.as_view(), name='detail'),
    url(r'^(?P<product_code>[\w-]+)/delete/$', SsdDelete.as_view(), name='delete'),
    url(r'^(?P<product_code>[\w-]+)/update/$', SsdUpdate.as_view(), name='update'),
]
