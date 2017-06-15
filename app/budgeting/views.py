# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import BudgetingForm
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Budgeting, Item

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

        return HttpResponseRedirect('/')
    form = BudgetingForm()
    return render(request, 'budgeting/create_budgeting.html', {'form':form})


def budgeting_items(request, pk):
    budgeting =  Budgeting.objects.get(id=pk)
    items = Item.objects.filter(budgeting=budgeting)
    return render(request, 'budgeting/items_budgeting.html', {'budgeting': budgeting, 'items':items})
