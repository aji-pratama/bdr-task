# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opreport', '0008_auto_20170519_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_flight', models.CharField(max_length=150)),
                ('om', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('customer', models.CharField(max_length=150)),
                ('id_jobno', models.CharField(max_length=150)),
                ('purpose', models.CharField(max_length=150)),
                ('cost', models.CharField(max_length=150)),
                ('payment', models.CharField(max_length=150)),
            ],
        ),
    ]
