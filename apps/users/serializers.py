# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 20:49
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    '''
    用户序列化类
    '''
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.CharField()
