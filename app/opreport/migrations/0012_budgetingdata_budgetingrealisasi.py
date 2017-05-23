# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opreport', '0011_cashadv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budgetingdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('coa', models.CharField(max_length=100)),
                ('deskripsi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BudgetingRealisasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('januari', 'Januari'), ('februari', 'Februari'), ('maret', 'Maret'), ('april', 'April'), ('mei', 'Mei'), ('juni', 'Juni'), ('juli', 'Juli'), ('agustus', 'Agustus'), ('september', 'September'), ('oktober', 'Oktober'), ('november', 'November'), ('desember', 'Desember')], max_length=100)),
                ('budgeting', models.CharField(max_length=100)),
                ('realisasi', models.CharField(max_length=100)),
                ('deskripsi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opreport.Budgetingdata')),
            ],
        ),
    ]