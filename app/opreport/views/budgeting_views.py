from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import BudgetingRealisasi
from app.opreport.forms import BudgetingRealisasiForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# LIST Data where location is Kendari
def index_budgeting_kendari(request):
    try:
        form = BudgetingRealisasiForm()
        budgeting_list = BudgetingRealisasi.objects.filter(location="Kendari").order_by('-id')
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
    return render(request, 'opreport/budgeting/index_kendari.html', {'budgetings': budgetings, 'form':form})

# LIST Data where location is Teluk Sirih
def index_budgeting_ts(request):
    try:
        form = BudgetingRealisasiForm()
        budgeting_list = BudgetingRealisasi.objects.filter(location="Teluk Sirih").order_by('-id')
        paginator = Paginator(budgeting_list, 5)
        page = request.GET.get('pagets')

        try:
            budgetings = paginator.page(page)
        except PageNotAnInteger:
            budgetings = paginator.page(1)
        except EmptyPage:
            budgetings = paginator.page(paginator.num_pages)

    except BudgetingRealisasi.DoesNotExist:
        raise Http404("BudgetingRealisasi Does Not Exist")
    return render(request, 'opreport/budgeting/index_ts.html', {'budgetings':budgetings, 'form':form})


def input_budgeting(request):
    if request.POST:
        location = request.POST.get('location')
        coa = request.POST.get('coa')
        deskripsi = request.POST.get('deskripsi')
        insert_data = BudgetingRealisasi(location=location,coa=coa,deskripsi=deskripsi,)
        insert_data.save()
        messages.add_message(request, messages.INFO, 'Budgeting %s telah ditambahkan' % deskripsi)
        return HttpResponseRedirect('/operation-report/input-budgeting')
    form = BudgetingRealisasiForm()
    return render(request, 'opreport/budgeting/new_budgeting.html', {'form':form})


def edit_budgeting(request, pk):
    budgeting = BudgetingRealisasi.objects.get(id=pk)
    form = BudgetingRealisasiForm()
    if request.POST:
        location = request.POST.get('location')
        coa = request.POST.get('coa')
        deskripsi = request.POST.get('deskripsi')

        budgeting.location = location
        budgeting.coa = coa
        budgeting.deskripsi = deskripsi
        budgeting.save()

        messages.add_message(request, messages.INFO, 'Budgeting %s telah diupdate' % deskripsi)
        return HttpResponseRedirect('/operation-report/edit-budgeting-%s' % budgeting.id)

    return render(request, 'opreport/budgeting/edit_budgeting.html', {'form':form, 'budgeting':budgeting})

def budgeting_realisasi(request, pk):
    budgeting = BudgetingRealisasi.objects.get(id=pk)
    if request.POST:
        januari_budgeting = request.POST.get('januari_budgeting')
        januari_realisasi = request.POST.get('januari_realisasi')
        februari_budgeting = request.POST.get('februari_budgeting')
        februari_realisasi = request.POST.get('februari_realisasi')
        maret_budgeting = request.POST.get('maret_budgeting')
        maret_realisasi = request.POST.get('maret_realisasi')
        april_budgeting = request.POST.get('april_budgeting')
        april_realisasi = request.POST.get('april_realisasi')
        mei_budgeting = request.POST.get('mei_budgeting')
        mei_realisasi = request.POST.get('mei_realisasi')
        juni_budgeting = request.POST.get('juni_budgeting')
        juni_realisasi = request.POST.get('juni_realisasi')
        juli_budgeting = request.POST.get('juli_budgeting')
        juli_realisasi = request.POST.get('juli_realisasi')
        agustus_budgeting = request.POST.get('agustus_budgeting')
        agustus_realisasi = request.POST.get('agustus_realisasi')
        september_budgeting = request.POST.get('september_budgeting')
        september_realisasi = request.POST.get('september_realisasi')
        oktober_budgeting = request.POST.get('oktober_budgeting')
        oktober_realisasi = request.POST.get('oktober_realisasi')
        november_budgeting = request.POST.get('november_budgeting')
        november_realisasi = request.POST.get('november_realisasi')
        desember_budgeting = request.POST.get('desember_budgeting')
        desember_realisasi = request.POST.get('desember_realisasi')

        budgeting.januari_budgeting = januari_budgeting
        budgeting.januari_realisasi = januari_realisasi
        budgeting.februari_budgeting = februari_budgeting
        budgeting.februari_realisasi = februari_realisasi
        budgeting.maret_budgeting = maret_budgeting
        budgeting.maret_realisasi = maret_realisasi
        budgeting.april_budgeting = april_budgeting
        budgeting.april_realisasi = april_realisasi
        budgeting.mei_budgeting = mei_budgeting
        budgeting.mei_realisasi = mei_realisasi
        budgeting.juni_budgeting = juni_budgeting
        budgeting.juni_realisasi = juni_realisasi
        budgeting.juli_budgeting = juli_budgeting
        budgeting.juli_realisasi = juli_realisasi
        budgeting.agustus_budgeting = agustus_budgeting
        budgeting.agustus_realisasi = agustus_realisasi
        budgeting.september_budgeting = september_budgeting
        budgeting.september_realisasi = september_realisasi
        budgeting.oktober_budgeting = oktober_budgeting
        budgeting.oktober_realisasi = oktober_realisasi
        budgeting.november_budgeting = november_budgeting
        budgeting.november_realisasi = november_realisasi
        budgeting.desember_budgeting = desember_budgeting
        budgeting.desember_realisasi = desember_realisasi

        budgeting.save()

        messages.add_message(request, messages.INFO, 'Budgeting telah diupdate')
        return HttpResponseRedirect('/operation-report/budgeting-realisasi-%s' % budgeting.id)

    return render(request, 'opreport/budgeting/budgeting_realisasi.html', {'budgeting':budgeting})

def delete_budgeting(request, pk):
    budgeting = BudgetingRealisasi.objects.get(id=pk)
    budgeting.delete()

    return HttpResponseRedirect('/operation-report/budgeting/')










#
