from django.contrib.auth.models import User

# Create your views here.
from rest_framework import status,viewsets

from idcs.models import Idc
from .serializers import IdcSerializer, UserSerializer

class IdcListViewset(viewsets.ModelViewSet):
    '''
    retrieve:
        返回指定Idc信息
    list:
        返回Idc列表
    update:
        更新Idc信息
    destroy:
        删除Idc记录
    create：
        创建Idcj记录
    partial_update:
        Idc局部更新
    '''
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer