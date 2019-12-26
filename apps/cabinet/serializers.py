# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 16:59
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers

from cabinet.models import Cabinet


class CabinetServerSerializer(serializers.Serializer):
    '''
    Cabinet序列化类
    '''
    id = serializers.IntegerField(read_only=True)
    province = serializers.CharField(required=True,max_length=32)
    city = serializers.CharField(required=True,max_length=32)
    engine_room = serializers.CharField(required=True,max_length=200)
    cabinet = serializers.CharField(required=True,max_length=200)
    server_equipment = serializers.CharField(required=True,max_length=200)
    service_ip = serializers.CharField(required=True,max_length=200)
    ipv6_service_ip = serializers.CharField(required=True,max_length=200)
    service_gateway = serializers.CharField(required=True,max_length=200)
    uplink_switch = serializers.CharField(required=True,max_length=200)
    switch_port = serializers.CharField(required=True,max_length=200)
    switch_location = serializers.CharField(required=True,max_length=200)

    def create(self, validated_data):
        return Cabinet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.provice = validated_data.get('provice',instance.provice)
        instance.city = validated_data.get('city', instance.city)
        instance.engine_room = validated_data.get('engine_room', instance.engine_room)
        instance.cabinet = validated_data.get('cabinet', instance.cabinet)
        instance.server_equipment = validated_data.get('server_equipment', instance.server_equipment)
        instance.service_ip = validated_data.get('service_ip', instance.service_ip)
        instance.ipv6_service_ip = validated_data.get('ipv6_service_ip', instance.ipv6_service_ip)
        instance.service_gateway = validated_data.get('service_gateway', instance.service_gateway)
        instance.uplink_switch = validated_data.get('uplink_switch', instance.uplink_switch)
        instance.switch_port = validated_data.get('switch_port', instance.switch_port)
        instance.switch_location = validated_data.get('switch_location', instance.switch_location)
        instance.save()
        return instance