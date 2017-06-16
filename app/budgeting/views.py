# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import BudgetingForm
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from .models import Budgeting, Item
from django.core import serializers
import json

def add_budgeting(request):
    if request.POST:
        unit = request.user.unit
        departement = request.user.departement
        divisi = request.user.divisi
        jobid = request.POST.get('jobid')
        nodoc = request.POST.get('nodoc')
        type_proposal = request.POST.get('type_proposal')
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        disc = request.POST.get('disc')
        tax = request.POST.get('tax')
        total_amount = request.POST.get('total_amount')
        remark = request.POST.get('remark')
        insert_data = Budgeting(unit=unit, departement=departement, divisi=divisi,
                                jobid=jobid, nodoc=nodoc, type_proposal=type_proposal,
                                date=date, amount=amount, disc=disc, tax=tax, total_amount=total_amount,
                                remark=remark)
        insert_data.save()
        idb = insert_data.id
        return HttpResponseRedirect('/budgeting/items-budgeting-%s' % idb)
    form = BudgetingForm()
    return render(request, 'budgeting/create_budgeting.html', {'form':form})


def budgeting_items(request, pk):
    budgeting =  Budgeting.objects.get(id=pk)
    items = Item.objects.filter(budgeting=budgeting)
    if request.POST:
        description = request.POST.get('description')
        qty = request.POST.get('qty')
        amount = request.POST.get('amount')
        tot_amount = request.POST.get('tot_amount')
        insert_data = Item(description=description,qty=qty,amount=amount,tot_amount=tot_amount, budgeting=budgeting)
        insert_data.save()
        return HttpResponseRedirect('/budgeting')
    return render(request, 'budgeting/items_budgeting.html', {'budgeting': budgeting, 'items':items})

def get_items(request):
    items = Item.objects.all()
    data = serializers.serialize('json', items)
    return HttpResponse(data, content_type='application/json')
