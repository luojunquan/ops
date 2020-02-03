# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 16:36
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : filter.py
# @Software: PyCharm
import django_filters
from django.contrib.auth.models import Group

class GroupFilter(django_filters.FilterSet):
    """
    Group:搜索类
    """
    name = django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        fields = ['name']
