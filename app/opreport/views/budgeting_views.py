from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import BudgetingRealisasi
# from app.opreport.forms import BudgetingdataForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_budgeting(request):
    try:
        # form = BudgetingdataForm()
        budgeting_list = BudgetingRealisasi.objects.all()

        paginator = Paginator(budgeting_list, 5)

        page = request.GET.get('page')
        try:
            budgetings = paginator.page(page)
        except PageNotAnInteger:
            budgetings = paginator.page(1)
        except EmptyPage:
            budgetings = paginator.page(paginator.num_pages)

    except BudgetingRealisasi.DoesNotExist:
        raise Http404("BudgetingRealisasi Does Not Exist")
    return render(request, 'opreport/budgeting/index_budgeting.html', {'budgetings': budgetings})

def input_budgeting(request):
    if request.POST:
        location = request.POST.get('location')
        coa = request.POST.get('coa')
        deskripsi = request.POST.get('deskripsi')
        insert_data = BudgetingRealisasi(location=location,coa=coa,deskripsi=deskripsi,)
        insert_data.save()
        return HttpResponse('')

def delete_budgeting(request, pk):
    budgeting = BudgetingRealisasi.objects.get(id=pk)
    budgeting.delete()

    return HttpResponseRedirect('/operation-report/budgeting/')










#
