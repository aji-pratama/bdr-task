from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Tender
from app.opreport.forms import TenderForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_tender(request):
    try:
        form = TenderForm()
        tender_list = Tender.objects.all()
        # if request.POST:
        #     q = request.POST.get('q')
        #     tender_list = Tender.objects.filter(tender_name__contains=q)

        paginator = Paginator(tender_list, 5) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            tenders = paginator.page(page)
        except PageNotAnInteger:
            tenders = paginator.page(1)
        except EmptyPage:
            tenders = paginator.page(paginator.num_pages)

    except Tender.DoesNotExist:
        raise Http404("Tender Does Not Exist")
    return render(request, 'opreport/tender/index_tender.html', {'tenders': tenders, 'form': form})

def input_tender(request):
    if request.POST:
        om = request.POST.get('om')
        quotation_no = request.POST.get('quotation_no')
        location = request.POST.get('location')
        tender_name = request.POST.get('tender_name')
        rks_no = request.POST.get('rks_no')
        process_registration = request.POST.get('process_registration')
        process_aanwizing = request.POST.get('process_aanwizing')
        process_openbid = request.POST.get('process_openbid')
        addcost_bidbond = request.POST.get('addcost_bidbond')
        addcost_reffbank = request.POST.get('addcost_reffbank')
        addcost_document = request.POST.get('addcost_document')
        remark = request.POST.get('remark')
        insert_data = Tender(om=om, quotation_no=quotation_no, location=location, tender_name=tender_name,
                    rks_no=rks_no, process_registration=process_registration, process_aanwizing=process_aanwizing,
                    process_openbid=process_openbid, addcost_bidbond=addcost_bidbond, addcost_reffbank=addcost_reffbank,
                    addcost_document=addcost_document, remark=remark)
        insert_data.save()
        return HttpResponse('')

def delete_tender(request, pk):
    tender = Tender.objects.get(id=pk)
    tender.delete()

    return HttpResponseRedirect('/operation-report/tender/')















#
