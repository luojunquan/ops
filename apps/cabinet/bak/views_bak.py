from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from cabinet.models import Cabinet
from cabinet.serializers import CabinetSerializer


class CabinetViewset(viewsets.ModelViewSet):
    '''
    retrieve:
        返回指定机柜信息
    list:
        返回机柜列表
    update:
        更新机柜信息
    destroy:
        删除机柜记录
    create：
        创建机柜记录
    partial_update:
        机柜局部更新
    '''
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
'''
@api_view(['GET'])
def api_root(request, format=None, *args, **kwargs):
    return Response({
        'cabinetserver': reverse('cabinetserver',request=request,format=format),
    })

class CabinetServer(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetServerSerializer
'''