from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Delivery
from app.opreport.forms import DeliveryForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def index_delivery(request):
    try:
        form = DeliveryForm()
        delivery_list = Delivery.objects.all()
        paginator = Paginator(delivery_list, 5)

        page = request.GET.get('page')
        try:
            deliverys = paginator.page(page)
        except PageNotAnInteger:
            deliverys = paginator.page(1)
        except EmptyPage:
            deliverys = paginator.page(paginator.num_pages)

    except Delivery.DoesNotExist:
        raise Http404("Delivery Does Not Exist")
    return render(request, 'opreport/delivery/index_delivery.html', {'deliverys': deliverys, 'form': form})

def input_delivery(request):
    if request.POST:
        om = request.POST.get('om')
        location = request.POST.get('location')
        job_no = request.POST.get('job_no')
        description_material = request.POST.get('description_material')
        vendor = request.POST.get('vendor')
        value_dpp = request.POST.get('value_dpp')
        value_ppn = request.POST.get('value_ppn')
        progress_dono = request.POST.get('progress_dono')
        progress_leadtime = request.POST.get('progress_leadtime')
        progress_pickup = request.POST.get('progress_pickup')
        expedisi = request.POST.get('expedisi')
        order_status = request.POST.get('order_status')
        insert_data = Delivery(om=om,location=location,job_no=job_no,description_material=description_material,
                    vendor=vendor,value_dpp=value_dpp,value_ppn=value_ppn,progress_dono=progress_dono,
                    progress_leadtime=progress_leadtime,progress_pickup=progress_pickup,expedisi=expedisi,
                    order_status=order_status)
        insert_data.save()
        messages.add_message(request, messages.INFO, 'Delivery %s telah ditambahkan' % location)
        return HttpResponseRedirect('/operation-report/input-delivery')
    form = DeliveryForm()
    return render(request, 'opreport/delivery/new_delivery.html', {'form':form})


def edit_delivery(request, pk):
    delivery = Delivery.objects.get(id=pk)
    form = DeliveryForm()
    if request.POST:
        om = request.POST.get('om')
        location = request.POST.get('location')
        job_no = request.POST.get('job_no')
        description_material = request.POST.get('description_material')
        vendor = request.POST.get('vendor')
        value_dpp = request.POST.get('value_dpp')
        value_ppn = request.POST.get('value_ppn')
        progress_dono = request.POST.get('progress_dono')
        progress_leadtime = request.POST.get('progress_leadtime')
        progress_pickup = request.POST.get('progress_pickup')
        expedisi = request.POST.get('expedisi')
        order_status = request.POST.get('order_status')

        delivery.om = om
        delivery.location = location
        delivery.job_no = job_no
        delivery.description_material = description_material
        delivery.vendor = vendor
        delivery.value_dpp = value_dpp
        delivery.value_ppn = value_ppn
        delivery.progress_dono = progress_dono
        delivery.progress_leadtime = progress_leadtime
        delivery.progress_pickup = progress_pickup
        delivery.expedisi = expedisi
        delivery.order_status = order_status

        delivery.save()
        messages.add_message(request, messages.INFO, 'Delivery %s telah diupdate' % location)
        return HttpResponseRedirect('/operation-report/edit-delivery-%s' % delivery.id)

    return render(request, 'opreport/delivery/edit_delivery.html', {'form':form, 'delivery':delivery})


def delete_delivery(request, pk):
    delivery = Delivery.objects.get(id=pk)
    delivery.delete()

    return HttpResponseRedirect('/operation-report/delivery/')














#
