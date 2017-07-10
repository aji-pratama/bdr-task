from django.contrib import admin
from django.conf.urls import url, include
from app.account import views as account_views
from app.task import views as task_views
from app.account.views import LoginView, LogOutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', account_views.index, name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
    url(r'^dashboard/$', account_views.dashboard, name='dashboard'),

    #Staff
    url(r'^input-task/$', task_views.input_task, name='input_task'),
    url(r'^edit-task-(?P<pk>\d+)$', task_views.edit_task, name='edit_task'),
    url(r'^delete-task-(?P<pk>\d+)$', task_views.delete_task, name='delete_task'),
    url(r'^doing-task/$', task_views.doing_task, name='doing_task'),
    url(r'^cek-done-(?P<pk>\d+)$', task_views.cek_done, name='cek_done'),
    url(r'^finish-today$', task_views.finish_today, name='finish_today'),

    #Atasan
    url(r'^task-approval/$', task_views.task_approval, name='task_approval'),
    url(r'^task-approval/task-by-user(?P<pk>\d+)$', task_views.task_by, name='task_by'),
    url(r'^task-approval/approve(?P<pk>\d+)/$', task_views.approve, name='approve'),
    url(r'^task-approval/cancel-approve(?P<pk>\d+)/$', task_views.cancel_approve, name='cancel_approve'),

    #asr
    url(r'^pkt/', include('app.pkt.pkt_urls')),

    #Operation Report
    url(r'^operation-report/', include('app.opreport.opreport_urls')),

    #Budgeting
    url(r'^budgeting/', include('app.budgeting.budgeting_urls')),

    #Testing way
    url(r'^testing/', include('app.testing.testing_urls')),

]
