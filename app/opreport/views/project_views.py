from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Project
from app.opreport.forms import ProjectForm
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    projects = Project.objects.all().order_by('id')
    form = ProjectForm()
    return render(request, 'opreport/index.html', {'projects': projects, 'form': form})

def forms(request):
    projects = Project.objects.all()
    form = ProjectForm()
    return render(request, 'opreport/forms.html', {'projects': projects, 'form':form})


def input_data(request):
    if request.POST:
        title = request.POST.get('title')
        om  = request.POST.get('om')
        location    = request.POST.get('location')
        job_no  = request.POST.get('job_no')
        project_name    = request.POST.get('project_name')
        spk_no  = request.POST.get('spk_no')
        value   = request.POST.get('value')
        statuspr_material   = request.POST.get('statuspr_material')
        statuspr_fabrication    = request.POST.get('statuspr_fabrication')
        statuspr_installation   = request.POST.get('statuspr_installation')
        invoice_tahap1  = request.POST.get('invoice_tahap1')
        invoice_tahap2  = request.POST.get('invoice_tahap2')
        invoice_tahap3  = request.POST.get('invoice_tahap3')
        remark = request.POST.get('remark')
        insert_data = Project(om=om,location=location, job_no=job_no,
                project_name=project_name, spk_no=spk_no, value=value,
                statuspr_material=statuspr_material, statuspr_fabrication=statuspr_fabrication,
                statuspr_installation=statuspr_installation, invoice_tahap1=invoice_tahap1,
                invoice_tahap2=invoice_tahap2, invoice_tahap3=invoice_tahap3, remark=remark)

        insert_data.save()
        return HttpResponse('')
