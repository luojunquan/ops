from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from manufacturer.models import Manufacturer, ProductModel
from manufacturer.serializers import ManufacturerSerializer, ProductModelSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    '''
    retrieve:
        返回指定制造商信息
    list:
        返回制造商列表
    update:
        更新制造商信息
    destroy:
        删除制造商记录
    create：
        创建制造商记录
    partial_update:
        制造商局部更新
    '''
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ProductModelViewSet(viewsets.ModelViewSet):
    '''
    retrieve:
        返回指定制造商信息
    list:
        返回制造商列表
    update:
        更新制造商信息
    destroy:
        删除制造商记录
    create：
        创建制造商记录
    partial_update:
        制造商局部更新
    '''
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer