# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data1', models.IntegerField()),
                ('data2', models.IntegerField()),
                ('data3', models.IntegerField()),
                ('data4', models.IntegerField()),
                ('data5', models.IntegerField()),
                ('data6', models.IntegerField()),
                ('data7', models.IntegerField()),
                ('data8', models.IntegerField()),
                ('data9', models.IntegerField()),
                ('data10', models.IntegerField()),
                ('data11', models.IntegerField()),
                ('data12', models.IntegerField()),
                ('data13', models.IntegerField()),
                ('data14', models.IntegerField()),
                ('data15', models.IntegerField()),
                ('data16', models.IntegerField()),
                ('data17', models.IntegerField()),
                ('data18', models.IntegerField()),
                ('data19', models.IntegerField()),
                ('data20', models.IntegerField()),
            ],
        ),
    ]
