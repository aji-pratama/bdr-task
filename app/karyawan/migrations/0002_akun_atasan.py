# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='akun',
            name='atasan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='karyawan.Akun'),
        ),
    ]