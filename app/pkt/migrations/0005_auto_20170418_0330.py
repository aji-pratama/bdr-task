# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkt', '0004_datas_hps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='hps',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]