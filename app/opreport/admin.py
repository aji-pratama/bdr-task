# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Project, Quotation
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['om', 'location', 'project_name']
	search_fields = ['om', 'location', 'project_name']
	list_per_page = 20

admin.site.register(Project, ProjectAdmin)

class QuotationAdmin(admin.ModelAdmin):
	list_display = ['costumer', 'tanggal']
	search_fields = ['costumer', 'tanggal']
	list_per_page = 20

admin.site.register(Quotation, QuotationAdmin)
