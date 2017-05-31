from django.conf.urls import url
from django.contrib import admin
from .views import (
                    CpuList,
                    CpuCreate,
                    CpuDetail,
                    CpuDelete,
                    CpuUpdate,
                    )

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', CpuList.as_view(), name='list'),
    url(r'^create/$', CpuCreate.as_view(), name='create'),
    url(r'^(?P<product_code>[\w-]+)/$', CpuDetail.as_view(), name='detail'),
    url(r'^(?P<product_code>[\w-]+)/delete/$', CpuDelete.as_view(), name='delete'),
    url(r'^(?P<product_code>[\w-]+)/update/$', CpuUpdate.as_view(), name='update'),
]
