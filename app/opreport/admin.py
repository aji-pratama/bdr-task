# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Project, Quotation, Tender, Delivery, Ticket, Cashadv, BudgetingRealisasi
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

class TenderAdmin(admin.ModelAdmin):
	list_display = ['om', 'quotation_no', 'location', 'tender_name']
	search_fields = ['om', 'quotation_no', 'location', 'tender_name']
	list_per_page = 20

admin.site.register(Tender, TenderAdmin)

#Admin Delivery
admin.site.register(Delivery)
admin.site.register(Ticket)
admin.site.register(Cashadv)
admin.site.register(BudgetingRealisasi)
