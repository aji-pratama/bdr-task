# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_atasan',
            field=models.BooleanField(default=False),
        ),
    ]