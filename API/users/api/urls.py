from django.conf.urls import url
from django.contrib import admin
from .views import (
                    UserDelete,
                    UserDetail,
                    UserList,
                    UserUpdate,
                    UserCreate,
                    )

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', UserList.as_view(), name='list'),
    url(r'^create/$', UserCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', UserDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', UserDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', UserUpdate.as_view(), name='update'),
]
