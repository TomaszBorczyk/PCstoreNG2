from django.conf.urls import url
from django.contrib import admin
from .views import (
                    UserAuthView,
                    )

urlpatterns = [
    url(r'^$', UserAuthView.as_view(), name='ulist'),
]


# from django.conf.urls import  url, include
# from rest_framework import routers
#
# from .views import UserAuthView
#
# router = routers.DefaultRouter()
# router.register(r'accounts', UserAuthView, 'list')
#
# urlpatterns = [
#     url(r'^api/', include(router.urls)),
# ]
