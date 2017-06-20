from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Cashadv
from app.opreport.forms import CashadvForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def index_cashadv(request):
    try:
        form = CashadvForm()
        cashadv_list = Cashadv.objects.all().order_by('-id')
        paginator = Paginator(cashadv_list, 5) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            cashadvs = paginator.page(page)
        except PageNotAnInteger:
            cashadvs = paginator.page(1)
        except EmptyPage:
            cashadvs = paginator.page(paginator.num_pages)

    except Cashadv.DoesNotExist:
        raise Http404("Cashadv Does Not Exist")
    return render(request, 'opreport/cashadv/index_cashadv.html', {'cashadvs': cashadvs, 'form': form})

def input_cashadv(request):
    if request.POST:
        date_request = request.POST.get('date_request')
        om = request.POST.get('om')
        name_of_payee = request.POST.get('name_of_payee')
        customer = request.POST.get('customer')
        id_jobno = request.POST.get('id_jobno')
        purpose = request.POST.get('purpose')
        car = request.POST.get('car')
        pi = request.POST.get('pi')
        actual_cost = request.POST.get('actual_cost')
        receive_payment = request.POST.get('receive_payment')
        status = request.POST.get('status')

        insert_data = Cashadv(date_request=date_request,om=om,name_of_payee=name_of_payee,customer=customer,
                            id_jobno=id_jobno,purpose=purpose,car=car,pi=pi,actual_cost=actual_cost,
                            receive_payment=receive_payment,status=status)
        insert_data.save()
        messages.add_message(request, messages.INFO, 'Cashadv %s telah ditambahkan' % date_request)
        return HttpResponseRedirect('/operation-report/input-cashadv')
    form = CashadvForm()
    return render(request, 'opreport/cashadv/new_cashadv.html', {'form':form})


def edit_cashadv(request, pk):
    cashadv = Cashadv.objects.get(id=pk)
    form = CashadvForm()
    if request.POST:
        date_request = request.POST.get('date_request')
        om = request.POST.get('om')
        name_of_payee = request.POST.get('name_of_payee')
        customer = request.POST.get('customer')
        id_jobno = request.POST.get('id_jobno')
        purpose = request.POST.get('purpose')
        car = request.POST.get('car')
        pi = request.POST.get('pi')
        actual_cost = request.POST.get('actual_cost')
        receive_payment = request.POST.get('receive_payment')
        status = request.POST.get('status')

        cashadv.date_request = date_request
        cashadv.om = om
        cashadv.name_of_payee = name_of_payee
        cashadv.customer = customer
        cashadv.id_jobno = id_jobno
        cashadv.purpose = purpose
        cashadv.car = car
        cashadv.pi = pi
        cashadv.actual_cost = actual_cost
        cashadv.receive_payment = receive_payment
        cashadv.status = status

        cashadv.save()

        messages.add_message(request, messages.INFO, 'Cashadv %s telah diupdate' % date_request)
        return HttpResponseRedirect('/operation-report/edit-cashadv-%s' % cashadv.id)

    return render(request, 'opreport/cashadv/edit_cashadv.html', {'form':form, 'cashadv':cashadv})

def delete_cashadv(request, pk):
    cashadv = Cashadv.objects.get(id=pk)
    cashadv.delete()

    return HttpResponseRedirect('/operation-report/cashadv/')












#
