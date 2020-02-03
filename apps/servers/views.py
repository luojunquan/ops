from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, permissions, response

from servers.filter import ServerFilter, NetworkDeviceFilter, IpFilter
from servers.models import Server, NetworkDevice, IP
from servers.serializers import NetworkDeviceSerializer, IPSerializer, ServerAutoReportSerializer, ServerSerializer



class ServerAutoReportViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    '''
    create：
        创建服务器记录
    '''
    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer
    permission_classes = (permissions.AllowAny,)

class ServerViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin):
    '''
    list:
    获取服务器列表

    create:
    创建服务器

    retrieve:
    获取指定服务器记录

    update:
    修改服务器记录
    '''
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_class = ServerFilter
    # filter_fields = ("hostname",)
    extra_perm_map = {
        "GET":['servers.view_server']
    }
    filter_class = ServerFilter
    filter_fields = ('hostname', 'idc', 'cabinet', "service", "server_purpose", "server_type")

    def get_queryset(self):
        queryset = super(ServerViewSet, self).get_queryset()
        queryset = queryset.order_by("id")
        return queryset

class NetworkDeviceViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        返回指定网卡信息
    list:
        返回网卡列表
    '''
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer
    filter_class = NetworkDeviceFilter
    filter_fields = ("name",)

class IPViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        返回指定IP信息
    list:
        返回IP列表
    '''
    queryset = IP.objects.all()
    serializer_class = IPSerializer
    filter_class = IpFilter
    filter_fields = ("ip_addr",)

class ServerCountViewset(viewsets.ViewSet,mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Server.objects.all()

    def list(self, request, *args, **kwargs):
        data = self.get_server_nums()
        return response.Response(data)

    def get_server_nums(self):
        ret = {
            "count": self.queryset.count(),
            "vm_host_num": self.queryset.filter(server_type__exact=0).count(),
            "phy_host_num": self.queryset.filter(server_type__exact=1).count(),
            "master_host_num": self.queryset.filter(server_type__exact=2).count()
        }
        return ret