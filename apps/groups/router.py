# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 16:11
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : router.py
# @Software: PyCharm
from rest_framework.routers import DefaultRouter
from .views import GroupsViewset

group_router = DefaultRouter()
group_router.register(r'Groups',GroupsViewset,basename='Groups')