from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Project
from app.opreport.forms import ProjectForm

def index(request):
    projects = Project.objects.all()
    form = ProjectForm()
    return render(request, 'opreport/index.html', {'projects': projects, 'form':form})
