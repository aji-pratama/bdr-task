# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import BudgetingForm
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Budgeting

class BudgetingCreate(CreateView):
    model = Budgeting
    form_class = BudgetingForm
    template_name = 'budgeting/create_budgeting.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.unit = self.request.user.unit
        form.instance.departement = self.request.user.departement
        form.instance.divisi = self.request.user.divisi
        return super(BudgetingCreate, self).form_valid(form)
