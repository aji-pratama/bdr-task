from django.conf.urls import url
from . import views

app_name = 'pkt'

urlpatterns = [
        url(r'^$', views.standard_docs, name='standard_docs'),
        url(r'^standard-docs$', views.standard_docs, name='standard_docs'),
        url(r'^mandatory$', views.mandatory, name='mandatory'),
        url(r'^financial$', views.financial, name='financial'),
        url(r'^mandatory-teknis$', views.mandatory_teknis, name='mandatory_teknis'),
        url(r'^summary$', views.summary, name='summary'),
]
