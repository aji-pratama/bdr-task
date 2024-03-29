# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('om', models.CharField(choices=[('east', 'East'), ('west', 'West')], max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('job_no', models.CharField(max_length=30)),
                ('project_name', models.TextField()),
                ('spk_no', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('statuspr_material', models.IntegerField(default=0)),
                ('statuspr_fabrication', models.IntegerField(default=0)),
                ('statuspr_installation', models.IntegerField(default=0)),
                ('invoice_tahap1', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_tahap2', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_tahap3', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
