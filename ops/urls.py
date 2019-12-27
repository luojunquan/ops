"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from idcs.views import IdcListViewset
from cabinet.views import CabinetViewset
from users.views import UserViewSet
from manufacturer.views import ManufacturerViewSet
from manufacturer.views import ProductModelViewSet

route = DefaultRouter()
route.register('idcs',IdcListViewset,basename='idcs')
route.register('users',UserViewSet,basename='users')
route.register('cabinet',CabinetViewset,basename='cabinet')
route.register('manufacturer',ManufacturerViewSet,basename='manufacturer')
route.register('productmodel',ProductModelViewSet,basename='productmodel')
urlpatterns = [
    url(r'^',include(route.urls)),
    url(r'^docs/',include_docs_urls('运维平台接口文档')),
]
