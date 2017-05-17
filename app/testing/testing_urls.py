from django.conf.urls import url
from . import views

app_name = 'testing'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^input_data/$', views.input_data, name='input_data'),
        url(r'^get_data/$', views.get_data, name='get_data'),
    ]
