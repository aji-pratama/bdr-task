from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Budgetingdata
from app.opreport.forms import BudgetingdataForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_budgeting(request):
    try:
        form = BudgetingdataForm()
        budgetingdata_list = Budgetingdata.objects.all()
        # if request.POST:
        #     q = request.POST.get('q')
        #     budgetingdata_list = Budgetingdata.objects.filter(budgetingdata_name__contains=q)

        paginator = Paginator(budgetingdata_list, 5) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            budgetingdatas = paginator.page(page)
        except PageNotAnInteger:
            budgetingdatas = paginator.page(1)
        except EmptyPage:
            budgetingdatas = paginator.page(paginator.num_pages)

    except Budgetingdata.DoesNotExist:
        raise Http404("Budgetingdata Does Not Exist")
    return render(request, 'opreport/budgeting/index_budgeting.html', {'budgetingdatas': budgetingdatas, 'form': form})

def input_budgetingdata(request):
    if request.POST:
        location = request.get('location')
        coa = request.get('coa')
        deskripsi = request.get('deskripsi')
        insert_data = Budgetingdata(location=location,coa=coa,deskripsi=deskripsi)
        insert_data.save()
        return HttpResponse('')

def delete_budgetingdata(request, pk):
    budgetingdata = Budgetingdata.objects.get(id=pk)
    budgetingdata.delete()

    return HttpResponseRedirect('/operation-report/budgeting/')














#
