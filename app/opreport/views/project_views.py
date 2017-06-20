from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Project
from app.opreport.forms import ProjectForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def index_project(request):
    try:
        form = ProjectForm()
        project_list = Project.objects.all().order_by('-id')
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
        messages.add_message(request, messages.INFO, 'Project %s telah ditambahkan' % project_name)
        return HttpResponseRedirect('/operation-report/input-project')
    form = ProjectForm()
    return render(request, 'opreport/project/new_project.html', {'form':form})

def edit_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm()
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
        project.om=om
        project.location=location
        project.job_no=job_no
        project.project_name=project_name
        project.spk_no=spk_no
        project.value=value
        project.statuspr_material=statuspr_material
        project.statuspr_fabrication=statuspr_fabrication
        project.statuspr_installation=statuspr_installation
        project.invoice_tahap1=invoice_tahap1
        project.invoice_tahap2=invoice_tahap2
        project.invoice_tahap3=invoice_tahap3
        project.remark=remark

        project.save()
        messages.add_message(request, messages.INFO, 'Project %s telah diupdate' % project_name)
        return HttpResponseRedirect('/operation-report/edit-project-%s' % project.id)

    return render(request, 'opreport/project/edit_project.html', {'project':project, 'form':form})


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()

    return HttpResponseRedirect('/operation-report/project')


















#
