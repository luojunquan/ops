# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 16:07
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : serilaizers.py
# @Software: PyCharm
from django.contrib.auth.models import Group
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(GroupSerializer, self).to_representation(instance)
        ret["users"] = instance.user_set.all().count()
        return ret

    class Meta:
        model = Group
        fields = ("id", "name")