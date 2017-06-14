# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Budgeting, Item
from django.contrib import admin

admin.site.register([Budgeting, Item])
# Register your models here.
