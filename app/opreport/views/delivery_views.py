from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Delivery
from app.opreport.forms import DeliveryForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_delivery(request):
    try:
        form = DeliveryForm()
        delivery_list = Delivery.objects.all()
        # if request.POST:
        #     q = request.POST.get('q')
        #     delivery_list = Delivery.objects.filter(delivery_name__contains=q)

        paginator = Paginator(delivery_list, 5) # Show 25 contacts per page

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
        return HttpResponse('')

def delete_delivery(request, pk):
    delivery = Delivery.objects.get(id=pk)
    delivery.delete()

    return HttpResponseRedirect('/operation-report/delivery/')














#
