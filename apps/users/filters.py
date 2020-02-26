# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 20:36
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : filters.py
# @Software: PyCharm
import django_filters

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group,Permission


User = get_user_model()


class UserFilter(django_filters.rest_framework.FilterSet):
    """
    用户过滤类
    """
    class Meta:
        model = User
        fields = ['username']


class GroupFilter(django_filters.rest_framework.FilterSet):
    """
    用户组过滤类
    """

    class Meta:
        model = Group
        fields = ['name']


class PermissionFilter(django_filters.rest_framework.FilterSet):
    """
    权限过滤类
    """

    class Meta:
        model = Permission
        fields = ['name', 'codename']