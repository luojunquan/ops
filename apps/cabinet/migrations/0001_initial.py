# Generated by Django 2.0.5 on 2019-12-27 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('idcs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idcs.Idc', verbose_name='所在机房')),
            ],
            options={
                'verbose_name': '机柜信息表',
                'db_table': 'resource_cabinet',
                'ordering': ['id'],
            },
        ),
    ]
