# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Task

class TaskAdmin (admin.ModelAdmin):
	list_display = ['title','approval_status','done_status','keterangan','created_date','created_by','doing_date']
	list_filter = ()
	list_per_page = 25

admin.site.register(Task, TaskAdmin)
