from django.conf.urls import url
from django.contrib import admin
from .views import (
                    GpuList,
                    GpuCreate,
                    GpuDetail,
                    GpuDelete,
                    GpuUpdate,
                    )

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', GpuList.as_view(), name='list'),
    url(r'^create/$', GpuCreate.as_view(), name='create'),
    url(r'^(?P<product_code>[\w-]+)/$', GpuDetail.as_view(), name='detail'),
    url(r'^(?P<product_code>[\w-]+)/delete/$', GpuDelete.as_view(), name='delete'),
    url(r'^(?P<product_code>[\w-]+)/update/$', GpuUpdate.as_view(), name='update'),
]
