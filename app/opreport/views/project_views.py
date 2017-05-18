from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Project
from app.opreport.forms import ProjectForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_project(request):
    try:
        form = ProjectForm()
        project_list = Project.objects.all()
        # if request.POST:
        #     q = request.POST.get('q')
        #     project_list = Project.objects.filter(om__contains=q)

        paginator = Paginator(project_list, 5) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)

    except Project.DoesNotExist:
        raise Http404("Category Does Not Exist")
    return render(request, 'opreport/project/index.html', {'projects': projects, 'form': form})

def input_project(request):
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

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()

    return HttpResponseRedirect('/operation-report/project')


















#
