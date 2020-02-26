# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 20:36
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : permissions.py
# @Software: PyCharm
from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsSuperUser(permissions.BasePermission):
    """
    Allows access only to super users.
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser
