# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-16 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0002_auto_20170614_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='coa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
