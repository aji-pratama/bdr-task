from django.contrib import admin
from django.conf.urls import url, include
from app.account import views as account_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', account_views.index, name='index'),
    url(r'^login', account_views.login, name='login'),
    url(r'^logout', account_views.logout, name='logout'),
    url(r'^dashboard', account_views.dashboard, name='dashboard'),

]
