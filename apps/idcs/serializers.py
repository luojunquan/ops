# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 20:27
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers

from idcs.models import Idc
from django.contrib.auth.models import User

class IdcSerializer(serializers.Serializer):
    '''
    Idc序列化类
    '''
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=32,label='机房名称',help_text='机房名称',
                                 error_messages={'blank':'机房名称不能为空','required':'这个字段为必要字段'})
    address = serializers.CharField(required=True, max_length=200,label='机房地址',help_text='机房地址',
                                    error_messages={'blank':'机房地址不能为空','required':'这个字段为必要字段'})
    phone = serializers.CharField(required=True, max_length=15,label='联系电话',help_text='联系电话',
                                  error_messages={'blank':'联系电话不能为空','required':'这个字段为必要字段'})
    email = serializers.EmailField(required=True,label='Email',help_text='Email',
                                   error_messages={'blank':'Email不能为空','required':'这个字段为必要字段'})
    letter = serializers.CharField(required=True, max_length=5,label='机房简称',help_text='机房简称',
                                   error_messages={'blank':'机房简称不能为空','required':'这个字段为必要字段'})

    def create(self, validated_data):
        return Idc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.letter = validated_data.get('letter', instance.letter)
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, max_length=32)
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance