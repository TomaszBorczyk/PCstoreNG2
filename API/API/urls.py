"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/users/', include('users.api.urls')),
    url(r'^api/authusers/', include('auth_user.api.urls')),
    url(r'^api/products/', include('products.api.urls')),
    url(r'^api/cpus/', include('cpus.api.urls')),
    url(r'^api/gpus/', include('gpus.api.urls')),
    url(r'^api/hdds/', include('hdds.api.urls')),
    url(r'^api/rams/', include('rams.api.urls')),
    url(r'^api/ssds/', include('ssds.api.urls')),
    url(r'^api/orders/', include('orders.api.urls')),
    url(r'^', include('angular.urls'))
]
