# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Pkt
from django.contrib import admin

class PktAdmin (admin.ModelAdmin):
	list_display = ['teks', 'koef', 'kode']
	search_fields = ['teks']
	list_per_page = 20

admin.site.register(Pkt, PktAdmin)
