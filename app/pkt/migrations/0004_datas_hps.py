# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkt', '0003_auto_20170417_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='datas',
            name='hps',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]