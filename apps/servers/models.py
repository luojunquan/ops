from django.db import models

# Create your models here.
from cabinet.models import Cabinet
from idcs.models import Idc
from manufacturer.models import Manufacturer, ProductModel


class Server(models.Model):
    ip = models.CharField('管理IP',max_length=15,db_index=True,unique=True,help_text='管理IP')
    hostname = models.CharField('主机名',max_length=20,db_index=True,unique=True,help_text='主机名')
    cpu = models.CharField('CPU',max_length=50,help_text='CPU')
    mem = models.CharField('内存', max_length=32, help_text='内存')
    disk = models.CharField('磁盘', max_length=200, help_text='磁盘')
    os = models.CharField('系统', max_length=50,help_text='系统')
    sn = models.CharField('SN', max_length=50,db_index=True,help_text='SN')
    manufacturer = models.ForeignKey(Manufacturer,verbose_name='制造商',on_delete=models.CASCADE,help_text='制造商')
    model_name = models.ForeignKey(ProductModel,verbose_name='服务器型号',on_delete=models.CASCADE, help_text='服务器型号')
    rmt_card_ip = models.CharField('管理管理卡IP', max_length=15, db_index=True,unique=True,help_text='管理管理卡IP')
    idc = models.ForeignKey(Idc,null=True,on_delete=models.CASCADE,verbose_name='所在机房',help_text='所在机房')
    cabinet = models.ForeignKey(Cabinet,null=True,on_delete=models.CASCADE,verbose_name='所在机柜',help_text='所在机柜')
    cabinet_position = models.CharField('机柜所在位置',null=True,max_length=20, help_text='机柜所在位置')
    uuid = models.CharField('UUID', max_length=50, db_index=True,unique=True, help_text='UUID')
    last_check = models.DateTimeField('检测时间', db_index=True,auto_now=True, help_text='检测时间')
    remark = models.CharField('备注', max_length=200, help_text='备注', null=True)
    server_type = models.IntegerField("机器类型", db_index=True, default=0, help_text="机器类型")
    def __str__(self):
        return self.ip

    class Meta:
        db_table = 'resource_server'
        ordering = ['id']
        permissions = {
            ("view_server","can view server"),
        }

class NetworkDevice(models.Model):
    '''
    网卡模型
    '''
    name = models.CharField('网卡设备名',max_length=20,db_index=True,help_text='网卡设备名')
    mac_address = models.CharField('MAC地址',max_length=30,db_index=True,help_text='MAC地址')
    host = models.ForeignKey(Server,on_delete=models.CASCADE,verbose_name='所在服务器',help_text='所在服务器')
    remark = models.CharField('备注',max_length=200,help_text='备注',null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resource_network_device'
        ordering = ['id']

class IP(models.Model):
    '''
    IP模型
    '''
    ip_addr = models.CharField('ip地址',max_length=15,db_index=True,unique=True,help_text='ip地址')
    ip6_addr = models.CharField('ipv6地址',null=True, max_length=45, db_index=True, unique=True,help_text='ipv6地址')
    netmask = models.CharField('子网掩码',max_length=15,help_text='子网掩码')
    gateway = models.CharField('网关地址',max_length=15,db_index=True,unique=True,help_text='网关地址')
    ip6_gateway = models.CharField('IPV6网关地址', null=True,max_length=45, db_index=True, unique=True, help_text='IPV6网关地址')
    device = models.ForeignKey(NetworkDevice,on_delete=models.CASCADE,verbose_name='所在网卡',help_text='所在网卡')
    remark = models.CharField('备注',max_length=200,help_text='备注',null=True)

    def __str__(self):
        return self.ip_addr

    class Meta:
        db_table = 'resource_ip'
        ordering = ['id']