# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 16:59
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers

from cabinet.models import Cabinet
from idcs.models import Idc

class CabinetSerializer(serializers.Serializer):
    idc = serializers.PrimaryKeyRelatedField(many=False,queryset=Idc.objects.all())
    #idc = serializers.SerializerMethodField()
    name = serializers.CharField(required=True)

    def to_representation(self, instance):
        #序列化转json
        idc_obj = instance.idc
        ret = super(CabinetSerializer, self).to_representation(instance)
        ret['idc'] = {
            'id':idc_obj.id,
            'name':idc_obj.name
        }
        return ret
    '''
    def get_idc(self,obj):
        #这种情况是readonly，不可更改的
        return {
            'id' : obj.id,
            'name' : obj.name
        }
    '''
    def to_internal_value(self, data):
        '''
        反序列化第一步：拿到的是提交过来的原始数据：Querydict=>request.GET,request.POST
        '''
        return super(CabinetSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        return Cabinet.objects.create(**validated_data)