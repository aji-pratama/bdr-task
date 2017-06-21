# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0012_auto_20170621_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='tot_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]