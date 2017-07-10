from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime, date, timedelta
from django.utils import formats
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.decorators import user_passes_test
from app.account.models import MyUser

#Page input Task just User as Staff can access
@login_required(login_url='/login')
@user_passes_test(lambda u:u.is_staf, login_url='/login')
def input_task(request):
    tasks = Task.objects.filter(created_by=request.user, approval_status=False, created_date=datetime.now().date()).order_by('-id')

    if request.POST:
        title = request.POST.get('title')
        approval_status = False
        done_status = False
        keterangan = request.POST.get('keterangan')
        created_date = date.today()
        created_by = request.user
        approval_by = request.user.atasan

        #If today is Friday then doing date is Monday, else just tomorrow
        if datetime.today().weekday() == 5:
            doing_date = date.today() + timedelta(days=3)
        else:
            doing_date = date.today() + timedelta(days=1)

        insert_data = Task(title=title, approval_status=approval_status, done_status=done_status, keterangan=keterangan, created_date=created_date, created_by=created_by, approval_by=approval_by, doing_date=doing_date)
        insert_data.save()

        return HttpResponseRedirect('/input-task')

    return render(request, 'staff/input_task.html', {'tasks': tasks, 'time' : date.today()})

# Page edit Task  before approvals
@login_required(login_url='/login')
@user_passes_test(lambda u:u.is_staf, login_url='/login')
def edit_task(request, pk):
    task_edit = Task.objects.get(id=pk)
    tasks = Task.objects.filter(created_by=request.user, approval_status=False, created_date=datetime.now().date()).order_by('-id')
    if request.POST:
        task_edit.title = request.POST.get('title')
        task_edit.keterangan = request.POST.get('keterangan')
        task_edit.updated_date = date.today()
        task_edit.save()
        return HttpResponseRedirect('/input-task')

    return render(request, 'staff/edit_task.html', {'tasks': tasks, 'time' : date.today(),
                                                    'task_edit': task_edit})


#Page delete Task for Staff just User as Staff can access
@login_required(login_url='/login')
@user_passes_test(lambda u:u.is_staf, login_url='/login')
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return HttpResponseRedirect('/input-task')

#Page Doing Task just User as Staff can access
@login_required(login_url='/login')
@user_passes_test(lambda u:u.is_staf, login_url='/login')
def doing_task(request):
    doing_tasks = Task.objects.filter(created_by=request.user, approval_status=True,
                                     done_status=False, doing_date=datetime.now().date()
                                     ).order_by('-id')
    done_tasks = Task.objects.filter(created_by=request.user, approval_status=True,
                                     done_status=True, doing_date=datetime.now().date()
                                     ).order_by('-id')

    return render(request, 'staff/doing_task.html', {'doing_tasks': doing_tasks, 'done_tasks': done_tasks })

#Page Cek Done Task just User as Staff can access
@login_required(login_url='/login')
@user_passes_test(lambda u:u.is_staf, login_url='/login')
def cek_done(request, pk):
    task = Task.objects.get(id=pk)
    task.done_status = True
    task.save()
    return HttpResponseRedirect('/doing-task')


#ATASAN Pages Access

#List of Staff who created Task Lists
@login_required(login_url='/login')
@user_passes_test(lambda u:u.is_atasan, login_url='/login')
def task_approval(request):
    staff_atasan = MyUser.objects.filter(atasan=request.user)
    return render(request, 'atasan/task_approval.html', {'staff_atasan': staff_atasan})

#Lists Task By
@login_required(login_url='/login')
@user_passes_test(lambda u:u.is_atasan, login_url='/login')
def task_by(request, pk):
    tasks = Task.objects.filter(created_by_id=pk, approval_status=False,
                                created_date=datetime.now().date()).order_by('-id')
    staf = MyUser.objects.get(id=pk)
    task_approved = Task.objects.filter(created_by_id=pk, approval_status=True,
                                created_date=datetime.now().date()).order_by('-id')
    return render(request, 'atasan/task_by.html', {'tasks' : tasks, 'staf': staf, 'task_approved': task_approved })

#Button To Approve Tasks
@login_required(login_url='/login')
@user_passes_test(lambda u:u.is_atasan, login_url='/login')
def approve(request, pk):
    task = Task.objects.get(id=pk)
    task.approval_status = True
    task.save()

    staf = task.created_by_id

    return HttpResponseRedirect('/task-approval/task-by-user%s' % staf)

@login_required(login_url='/login')
@user_passes_test(lambda u:u.is_atasan, login_url='/login')
def cancel_approve(request, pk):
    task = Task.objects.get(id=pk)
    task.approval_status = False
    task.save()

    staf = task.created_by_id

    return HttpResponseRedirect('/task-approval/task-by-user%s' % staf)























#
