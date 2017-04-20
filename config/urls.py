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
    url(r'^input-task/$', task_views.input_task, name='input_task'),

    #asr
    url(r'^pkt/', include('app.pkt.pkt_urls')),

]
