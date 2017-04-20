from __future__ import unicode_literals
from django.shortcuts import render
from datetime import datetime
from django.utils import formats
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required(login_url='/login')
def input_task(request):
    if request.POST:
        title = request.POST.get('title')
        approval_status = False
        done_status = False
        keterangan = request.POST.get('keterangan')
        created_date = datetime.now()
        created_by = request.user#request.user
        approval_by = request.user.atasan#Atasans.objects.get(id=created_by.atasan_staff_id)#request.user.atasan_staff
        doing_date = datetime.now() #+ datetime.timedelta(days=1)

        insert_data = Task(title=title, approval_status=approval_status, done_status=done_status, keterangan=keterangan, created_date=created_date, created_by=created_by, approval_by=approval_by, doing_date=doing_date)
        insert_data.save()

        return render(request, 'staff/input_task.html')

    return render(request, 'staff/input_task.html')
