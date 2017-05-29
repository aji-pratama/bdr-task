from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Quotation
from app.opreport.forms import QuotationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def index_quotation(request):
    try:
        form = QuotationForm()
        quotation_list = Quotation.objects.all()
        paginator = Paginator(quotation_list, 5) # Show 5 contacts per page

        page = request.GET.get('page')
        try:
            quotations = paginator.page(page)
        except PageNotAnInteger:
            quotations = paginator.page(1)
        except EmptyPage:
            quotations = paginator.page(paginator.num_pages)

    except Quotation.DoesNotExist:
        raise Http404("Quotation Does Not Exist")
    return render(request, 'opreport/quotation/index_quotation.html', {'quotations': quotations, 'form': form})

def input_quotation(request):
    if request.POST:
        tanggal = request.POST.get('tanggal')
        inquiry_no = request.POST.get('inquiry_no')
        quotation_no = request.POST.get('quotation_no')
        costumer = request.POST.get('costumer')
        desc_material = request.POST.get('desc_material')
        qty = request.POST.get('qty')
        unit = request.POST.get('unit')
        bid_price = request.POST.get('bid_price')
        status = request.POST.get('status')
        insert_data = Quotation(tanggal=tanggal,inquiry_no=inquiry_no,
                    quotation_no=quotation_no,costumer=costumer,desc_material=desc_material,
                    qty=qty,unit=unit,bid_price=bid_price,status=status)
        insert_data.save()
        messages.add_message(request, messages.INFO, 'Quotation %s telah ditambahkan' % quotation_no)
        return HttpResponseRedirect('/operation-report/input-quotation')

    form = QuotationForm()
    return render(request, 'opreport/quotation/new_quotation.html', {'form':form})

def edit_quotation(request, pk):
    quotation = Quotation.objects.get(id=pk)
    form = QuotationForm()
    if request.POST:
        tanggal = request.POST.get('tanggal')
        inquiry_no = request.POST.get('inquiry_no')
        quotation_no = request.POST.get('quotation_no')
        costumer = request.POST.get('costumer')
        desc_material = request.POST.get('desc_material')
        qty = request.POST.get('qty')
        unit = request.POST.get('unit')
        bid_price = request.POST.get('bid_price')
        status = request.POST.get('status')

        quotation.tanggal = tanggal
        quotation.inquiry_no = inquiry_no
        quotation._no = quotation_no
        quotation.costumer = costumer
        quotation.desc_material = desc_material
        quotation.qty = qty
        quotation.unit = unit
        quotation.bid_price = bid_price
        quotation.status = status

        quotation.save()
        messages.add_message(request, messages.INFO, 'Quotation %s telah diupdate' % quotation_no)
        return HttpResponseRedirect('/operation-report/edit-quotation-%s' % quotation.id)

    return render(request, 'opreport/quotation/edit_quotation.html', {'form':form, 'quotation':quotation})

def delete_quotation(request, pk):
    quotation = Quotation.objects.get(id=pk)
    quotation.delete()

    return HttpResponseRedirect('/operation-report/quotation/')


















#
