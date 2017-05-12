from django.shortcuts import render, render_to_response
from .models import Pkt, Datas
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import xlwt
# from app.account.models import MyUser
# from django.contrib.auth.models import User

def standard_docs(request):
    try:
        datas = Datas.objects.get(id=1)
    except Exception:
        datas = Datas(id=1, data1=1)
        datas.save()
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

        datas = Datas.objects.get(id=1)
        datas.data1=data1
        datas.data2=data2
        datas.data3=data3
        datas.data4=data4
        datas.data5=data5
        datas.data6=data6
        datas.data7=data7
        datas.data8=data8
        datas.data9=data9
        datas.data10=data10

        datas.save()
        return HttpResponseRedirect('mandatory')

    pkt_data = Pkt.objects.filter(kode='standard')
    return render(request, 'pkt/standard_docs.html', {'pkt_data': pkt_data})

def mandatory(request):
    if request.POST:
        data11 = str(request.POST.get('data11'))
        data12 = str(request.POST.get('data12'))
        data13 = str(request.POST.get('data13'))
        data14 = str(request.POST.get('data14'))
        hps = request.POST.get('hps')

        datas = Datas.objects.get(id=1)

        datas.data11=data11
        datas.data12=data12
        datas.data13=data13
        datas.data14=data14
        datas.hps = hps

        datas.save()

        return HttpResponseRedirect('financial')

    pkt_data = Pkt.objects.filter(kode='mandatory')
    return render(request, 'pkt/mandatory.html', {'pkt_data': pkt_data})

def financial(request):
    if request.POST:
        data15 = str(request.POST.get('data15'))
        data16 = str(request.POST.get('data16'))
        data17 = str(request.POST.get('data17'))

        datas = Datas.objects.get(id=1)

        datas.data15=data15
        datas.data16=data16
        datas.data17=data17

        datas.save()
        return HttpResponseRedirect('mandatory-teknis')

    pkt_data = Pkt.objects.filter(kode='finance')
    return render(request, 'pkt/financial.html', {'pkt_data': pkt_data})

def mandatory_teknis(request):
    if request.POST:
        data18 = str(request.POST.get('data18'))
        data19 = str(request.POST.get('data19'))
        data20 = str(request.POST.get('data20'))

        datas = Datas.objects.get(id=1)

        datas.data18=data18
        datas.data19=data19
        datas.data20=data20

        datas.save()

        return HttpResponseRedirect('summary')

    pkt_data = Pkt.objects.filter(kode='mandatory_tek')
    return render(request, 'pkt/mandatory_teknis.html', {'pkt_data': pkt_data})

def summary(request):
    datas = Datas.objects.get(id=1)
    # for data in datas:
    count1 = datas.data1 + datas.data2 + datas.data3 + datas.data4 + datas.data5 + datas.data6 + datas.data7 + datas.data8 + datas.data9 + datas.data10 + datas.data11 + datas.data12 + datas.data13 + datas.data14 + datas.data15 + datas.data16 + datas.data17
    count2 = datas.data18 + datas.data19 + datas.data20
    hps = 0
    hps = datas.hps
    ranges = ""
    if hps >= 500000000 and hps <= 1000000000:
        ranges = "Kecil"
    elif hps >= 1000000001 and hps <= 3000000000:
        ranges = "Sedang"
    elif hps >= 3000000001 and hps <= 5000000000:
        ranges = "Besar"
    elif hps > 5000000000:
        ranges = "BOD"
    elif hps == 0:
        ranges = "Data Kosong"
    else:
        ranges = "Data dibawah ketentuan"
    return render(request, 'pkt/summary.html', {'datas': datas, 'count1': count1, 'count2':count2, 'hps': hps, 'ranges':ranges })


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Koefisien')
    wr = wb.add_sheet('Poin Hasil Peritungan')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['TEKS', 'KOEFISIEN']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    #Data Koef
    rows = Pkt.objects.all().values_list('teks', 'koef')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    #HPS
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    rowds = Datas.objects.all().values_list('hps')
    for rowd in rowds:
        row_num += 2
        for col_num in range(len(rowd)):
            ws.write(row_num, 1, rowd[col_num], font_style)

    ws.write(row_num, 0, 'Harga Prakiraan Sementara', font_style)


    #Sheet2
    wr.write(1,0,'Poin Hasil Perhitungan', font_style)
    wr.write(2,0,'Kategori HPS', font_style)


    #Data
    datas = Datas.objects.get(id=1)
    # for data in datas:
    count1 = datas.data1 + datas.data2 + datas.data3 + datas.data4 + datas.data5 + datas.data6 + datas.data7 + datas.data8 + datas.data9 + datas.data10 + datas.data11 + datas.data12 + datas.data13 + datas.data14 + datas.data15 + datas.data16 + datas.data17
    count2 = datas.data18 + datas.data19 + datas.data20
    count = count1 + count2

    hps = 0
    hps = datas.hps

    #Ranges Category
    ranges = ""
    if hps >= 500000000 and hps <= 1000000000:
        ranges = "Kecil"
    elif hps >= 1000000001 and hps <= 3000000000:
        ranges = "Sedang"
    elif hps >= 3000000001 and hps <= 5000000000:
        ranges = "Besar"
    elif hps > 5000000000:
        ranges = "BOD"
    elif hps == 0:
        ranges = "Data Kosong"
    else:
        ranges = "Data dibawah ketentuan"

    wr.write(1,1, count)
    wr.write(2,1, ranges)

    wr.write(5,0, 'Pre Calculating')

    wb.save(response)
    return response
