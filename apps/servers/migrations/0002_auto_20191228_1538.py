# Generated by Django 2.0.5 on 2019-12-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='ip6_addr',
            field=models.CharField(db_index=True, help_text='ipv6地址', max_length=45, null=True, unique=True, verbose_name='ipv6地址'),
        ),
        migrations.AlterField(
            model_name='ip',
            name='ip6_gateway',
            field=models.CharField(db_index=True, help_text='IPV6网关地址', max_length=45, null=True, unique=True, verbose_name='IPV6网关地址'),
        ),
        migrations.AlterField(
            model_name='server',
            name='uuid',
            field=models.CharField(db_index=True, help_text='UUID', max_length=50, unique=True, verbose_name='UUID'),
        ),
    ]
