# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkt', '0005_auto_20170418_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='hps',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]