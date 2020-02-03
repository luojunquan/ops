# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 16:10
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from manufacturer.models import Manufacturer, ProductModel
from servers.models import Server, NetworkDevice, IP


class ServerAutoReportSerializer(serializers.Serializer):
    '''
    服务器自动同步序列化
    '''
    ip = serializers.IPAddressField(required=True)
    hostname = serializers.CharField(required=True,max_length=20)
    cpu = serializers.CharField(required=True,max_length=50)
    mem = serializers.CharField(required=True,max_length=20)
    disk = serializers.CharField(required=True,max_length=200)
    os = serializers.CharField(required=True,max_length=50)
    sn = serializers.CharField(required=True, max_length=50)
    manufacturer = serializers.CharField(required=True)
    model_name = serializers.CharField(required=True)
    uuid = serializers.CharField(required=True, max_length=50)
    #临时新增一个network的JSON序列化
    network = serializers.JSONField(required=True)

    #判断制造商是否存在，（字段级别验证）
    def validate_manufacturer(self, value):
        try:
            return Manufacturer.objects.get(vendor_name__exact=value)
        except Manufacturer.DoesNotExist:
            return self.create_manufacturer(value)
    #对象级别验证
    def validate(self, attrs):
        manufacturer_obj = attrs['manufacturer']
        try:
            attrs['model_name'] = manufacturer_obj.productmodel_set.get(model_name__exact=attrs['model_name'])
        except ProductModel.DoesNotExist:
            attrs['model_name'] = self.create_product_model(manufacturer_obj,attrs['model_name'])
        return attrs
    def to_representation(self, instance):
        ret = {
            "hostname" : instance.hostname,
            "ip" : instance.ip
        }
        return ret
    #如果验证没有制造商则创建
    def create_manufacturer(self,vendor_name):
        return Manufacturer.objects.create(vendor_name=vendor_name)
    # 如果验证没有服务器型号则创建
    def create_product_model(self,manufacturer_obj,model_name):
        return ProductModel.objects.create(model_name=model_name,vendor=manufacturer_obj)

    def check_service_network_device(self,server_obj,network):
        '''
        检查指定服务器有没有这些网卡设备，并做关联
        '''
        network_device_queryset = server_obj.networkdevice_set.all()
        current_network_device_queryset = []
        for device in network:
            try:
                #以网卡设备名为唯一标识
                network_device_obj = network_device_queryset.get(name__exact=device['name'])
            except NetworkDevice.DoesNotExist:
                #网卡不存在则创建
                network_device_obj = self.create_network_device(server_obj,device)

            self.check_ip(network_device_obj,device["ips"])
            current_network_device_queryset.append(network_device_obj)
        for network_device_obj in list(set(network_device_queryset) - set(current_network_device_queryset)):
            network_device_obj.delete()

    #检查IP是否在网卡中
    def check_ip(self,network_device_obj,ifnets):
        #拿到所有的IP
        ip_queryset = network_device_obj.ip_set.all()
        current_ip_queryset = []
        for ifnet in ifnets:
            try:
                ip_obj = ip_queryset.get(ip_addr__exact=ifnet['ip_addr'])
            except IP.DoesNotExist:
                ip_obj = self.create_ip(network_device_obj,ifnet)
            current_ip_queryset.append(ip_obj)
        #更新的和旧的相比，取差集，也就是旧的里面有的而在新的里面没有
        for ip_obj in list(set(ip_queryset) - set(current_ip_queryset)):
            ip_obj.delete()

    def create_server(self, validated_data):
        network = validated_data.pop('network')
        server_obj = Server.objects.create(**validated_data)
        self.check_service_network_device(server_obj,network)
        return server_obj

    def create(self, validated_data):
        uuid = validated_data['uuid'].lower()
        sn = validated_data['sn'].lower()
        try:
            if sn == uuid or sn == "" or sn.startwith("vmware"):
                #虚拟机
                server_obj = Server.objects.get(uuid__icontains=uuid)
            else:
                #物理机
                server_obj = Server.objects.get(sn__icontains=sn)
        except Server.DoesNotExist:
            return self.create_server(validated_data)
        else:
            return self.update_server(server_obj,validated_data)

    #创建网卡设备
    def create_network_device(self, server_obj, device):
        ips = device.pop('ips')
        #host为必传的值，在models里设置的是不为空
        device['host'] = server_obj
        network_device_obj = NetworkDevice.objects.create(**device)
        return network_device_obj
    def create_ip(self, network_device_obj, ifnet):
        ifnet['device'] = network_device_obj
        return IP.objects.create(**ifnet)

    #更新server
    def update_server(self, instance, validated_data):
        instance.hostname = validated_data.get('hostname',instance.hostname)
        instance.cpu = validated_data.get('cpu', instance.cpu)
        instance.ip = validated_data.get('ip', instance.ip)
        instance.mem = validated_data.get('mem', instance.mem)
        instance.disk = validated_data.get('disk', instance.disk)
        instance.os = validated_data.get('os', instance.os)
        instance.save()
        self.check_service_network_device(instance,validated_data['network'])
        return instance

class ServerSerializer(serializers.ModelSerializer):
    '''
    服务器序列化类
    '''
    last_check = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)
    def to_representation(self, instance):
        ret = super(ServerSerializer, self).to_representation(instance)
        ret['device'] = self.get_network_device(instance)
        return ret

    def get_network_device(self, server_obj):
        ret = []
        network_device = server_obj.networkdevice_set.all()
        for device in network_device:
            data = {
                "name": device.name,
                "mac": device.mac_address,
                "ips": self.get_ip(device)
            }
            ret.append(data)
        return ret

    def get_ip(self, network_device_obj):
        ret = []
        for ifnet in network_device_obj.ip_set.all():
            data = {
                "ip": ifnet.ip_addr,
                "netmask":ifnet.netmask,
                "gateway": ifnet.gateway,
                "ipv6": ifnet.ip6_addr,
                "ipv6_gateway": ifnet.ip6_gateway,
            }
            ret.append(data)
        return ret

    class Meta:
        model = Server
        fields = "__all__"

class NetworkDeviceSerializer(serializers.ModelSerializer):
    """
    网卡设备序列化类
    """
    def get_host(self, obj):
        try:
            return {
                "hostname": obj.hostname,
                "id": obj.id
            }
        except Exception as e:
            return {}

    def to_representation(self, instance):
        host = self.get_host(instance.host)
        ret = super(NetworkDeviceSerializer, self).to_representation(instance)
        ret["host"] = host
        return ret

    class Meta:
        model = NetworkDevice
        fields = "__all__"

class IPSerializer(serializers.ModelSerializer):
    """
    IP实例化类
    """
    def get_device(self, obj):
        try:
            return {
                "name": obj.name,
                "id": obj.id
            }
        except Exception as e:
            return {}

    def to_representation(self, instance):
        device = self.get_device(instance.device)
        ret = super(IPSerializer, self).to_representation(instance)
        ret["device"] = device
        return ret

    class Meta:
        model = IP
        fields = "__all__"
