# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 04:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opreport', '0004_tender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tender',
            old_name='process_egistration',
            new_name='process_openbid',
        ),
        migrations.RenameField(
            model_name='tender',
            old_name='process_penbid',
            new_name='process_registration',
        ),
    ]