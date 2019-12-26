# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 16:30
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from cabinet import views
from cabinet.views import CabinetServer

route = DefaultRouter()
route.register('cabinetserver',views.CabinetServer)
urlpatterns = [
    url(r'^',include(route.urls)),
    url(r'cabinetserver/$',CabinetServer.as_view,name='cabinetserver')
]