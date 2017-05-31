from django.conf.urls import url
from django.contrib import admin
from .views import (
                    HddList,
                    HddCreate,
                    HddDetail,
                    HddDelete,
                    HddUpdate,
                    )

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', HddList.as_view(), name='list'),
    url(r'^create/$', HddCreate.as_view(), name='create'),
    url(r'^(?P<product_code>[\w-]+)/$', HddDetail.as_view(), name='detail'),
    url(r'^(?P<product_code>[\w-]+)/delete/$', HddDelete.as_view(), name='delete'),
    url(r'^(?P<product_code>[\w-]+)/update/$', HddUpdate.as_view(), name='update'),
]
