from django.db import models

# Create your models here.
from django.db import models

from idcs.models import Idc


class Cabinet(models.Model):
    idc = models.ForeignKey(Idc,verbose_name='所在机房',on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机柜信息表'
        db_table = 'resource_cabinet'
        ordering = ['id']
