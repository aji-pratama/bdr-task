from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import BudgetingRealisasi
from app.opreport.forms import BudgetingRealisasiForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_budgeting(request):
    try:
        form = BudgetingRealisasiForm()
        budgeting_kendari_list = BudgetingRealisasi.objects.filter(location="Kendari")
        budgeting_ts_list = BudgetingRealisasi.objects.filter(location="Teluk Sirih")

        paginator_kendari = Paginator(budgeting_kendari_list, 5)
        paginator_ts = Paginator(budgeting_ts_list, 5)


        page_kendari = request.GET.get('page')
        page_ts = request.GET.get('pagets')

        try:
            budgetings_kendari = paginator_kendari.page(page_kendari)
            budgetings_ts = paginator_ts.page(page_ts)
        except PageNotAnInteger:
            budgetings_kendari = paginator_kendari.page(1)
            budgetings_ts = paginator_ts.page(1)
        except EmptyPage:
            budgetings_kendari = paginator_kendari.page(paginator_kendari.num_pages)
            budgetings_ts = paginator_ts.page(paginator_ts.num_pages)

    except BudgetingRealisasi.DoesNotExist:
        raise Http404("BudgetingRealisasi Does Not Exist")
    return render(request, 'opreport/budgeting/index_budgeting.html', {'budgetings_kendari': budgetings_kendari, 'budgetings_ts':budgetings_ts, 'form':form})

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
