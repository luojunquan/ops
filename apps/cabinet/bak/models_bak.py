from django.db import models

# Create your models here.
from django.db import models

class Cabinet(models.Model):
    province = models.CharField(max_length=32,verbose_name='省份',)
    city = models.CharField(max_length=32,verbose_name='地市')
    engine_room = models.CharField(max_length=200,verbose_name='机房位置')
    cabinet = models.CharField(max_length=200,verbose_name='机柜')
    server_equipment = models.CharField(max_length=200,verbose_name='服务器型号')
    service_ip = models.CharField(max_length=200,verbose_name='服务器ip')
    ipv6_service_ip = models.CharField(max_length=200,verbose_name='服务器ipv6',null=True)
    service_gateway = models.CharField(max_length=200,verbose_name='服务器网关')
    uplink_switch = models.CharField(max_length=200,verbose_name='上联交换机')
    switch_port = models.CharField(max_length=200,verbose_name='交换机端口')
    switch_location = models.CharField(max_length=200,verbose_name='交换机位置')

    class Meta:
        verbose_name = '机柜服务器信息表'
        db_table = 'cabinet_server'
