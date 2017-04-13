from django.shortcuts import render, render_to_response
from .models import Pkt
from django.template import RequestContext
from django.http import HttpResponseRedirect

data_global = []
def standard_docs(request):
    if request.POST:
        data1 = str(request.POST.get('data1'))
        data2 = str(request.POST.get('data2'))
        data3 = str(request.POST.get('data3'))
        data4 = str(request.POST.get('data4'))
        data5 = str(request.POST.get('data5'))
        data6 = str(request.POST.get('data6'))
        data7 = str(request.POST.get('data7'))
        data8 = str(request.POST.get('data8'))
        data9 = str(request.POST.get('data9'))
        data10 = str(request.POST.get('data10'))

        insert_data = {'data1':data1, 'data2':data2,
                       'data3':data3, 'data4':data4,
                       'data5':data5, 'data6':data6,
                       'data7':data7, 'data8':data8,
                       'data9':data9, 'data10':data10, }

        datas = [i for i in data_global]

        datas.append(insert_data)
        data_global.append(insert_data)
        return HttpResponseRedirect('mandatory')

    pkt_data = Pkt.objects.filter(kode='standard')
    return render(request, 'pkt/standard_docs.html', {'pkt_data': pkt_data})

def mandatory(request):
    if request.POST:
        data11 = str(request.POST.get('data11'))
        data12 = str(request.POST.get('data12'))
        data13 = str(request.POST.get('data13'))
        data14 = str(request.POST.get('data14'))
        insert_data = {'data11':data11, 'data12':data12,
                       'data13':data13, 'data14':data14, }

        datas = [i for i in data_global]

        datas.append(insert_data)
        data_global.append(insert_data)
        return HttpResponseRedirect('financial')

    pkt_data = Pkt.objects.filter(kode='mandatory')
    return render(request, 'pkt/mandatory.html', {'pkt_data': pkt_data})

def financial(request):
    if request.POST:
        data15 = str(request.POST.get('data15'))
        data16 = str(request.POST.get('data16'))
        data17 = str(request.POST.get('data17'))
        insert_data = {'data15':data15, 'data16':data16,
                       'data17':data17,}

        datas = [i for i in data_global]

        datas.append(insert_data)
        data_global.append(insert_data)
        return HttpResponseRedirect('mandatory-teknis')

    pkt_data = Pkt.objects.filter(kode='finance')
    return render(request, 'pkt/financial.html', {'pkt_data': pkt_data})

def mandatory_teknis(request):
    pkt_data = Pkt.objects.filter(kode='mandatory_tek')
    return render(request, 'pkt/mandatory_teknis.html', {'pkt_data': pkt_data})

def summary(request):
    datas = [i for i in data_global]
    return render(request, 'pkt/summary.html', {'data_global': data_global, 'datas': datas})
