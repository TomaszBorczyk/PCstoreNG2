from django.conf.urls import url
from django.contrib import admin
from .views import (
                    RamList,
                    RamCreate,
                    RamDetail,
                    RamDelete,
                    RamUpdate,
                    )

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', RamList.as_view(), name='list'),
    url(r'^create/$', RamCreate.as_view(), name='create'),
    url(r'^(?P<product_code>[\w-]+)/$', RamDetail.as_view(), name='detail'),
    url(r'^(?P<product_code>[\w-]+)/delete/$', RamDelete.as_view(), name='delete'),
    url(r'^(?P<product_code>[\w-]+)/update/$', RamUpdate.as_view(), name='update'),
]
