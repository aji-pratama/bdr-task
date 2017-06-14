# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budgeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodoc', models.CharField(max_length=40)),
                ('type_proposal', models.CharField(choices=[('ADM', 'ADM'), ('OPR', 'OPR')], max_length=26)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('disc', models.DecimalField(decimal_places=2, max_digits=3)),
                ('tax', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('remark', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coa', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=220)),
                ('qty', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('tot_amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('budgeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgeting.Budgeting')),
            ],
            options={
                'ordering': ('description',),
            },
        ),
    ]
