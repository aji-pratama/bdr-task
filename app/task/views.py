from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from django.utils import formats
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required(login_url='/login')
def input_task(request):
    tasks = Task.objects.filter(created_by=request.user, created_date=datetime.now().date()).order_by('-id')

    if request.POST:
        title = request.POST.get('title')
        approval_status = False
        done_status = False
        keterangan = request.POST.get('keterangan')
        created_date = datetime.now()
        created_by = request.user
        approval_by = request.user.atasan
        doing_date = datetime.now()

        insert_data = Task(title=title, approval_status=approval_status, done_status=done_status, keterangan=keterangan, created_date=created_date, created_by=created_by, approval_by=approval_by, doing_date=doing_date)
        insert_data.save()

        return HttpResponseRedirect('/input-task')

    return render(request, 'staff/input_task.html', {'tasks': tasks})

@login_required(login_url='/login')
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    # messages.add_message(request, messages.INFO, 'Product %s deleted' % product.name)
    task.delete()

    return HttpResponseRedirect('/input-task')
