# Generated by Django 2.0.5 on 2019-12-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet',
            name='ipv6_service_ip',
            field=models.CharField(max_length=200, null=True, verbose_name='服务器ipv6'),
        ),
    ]
