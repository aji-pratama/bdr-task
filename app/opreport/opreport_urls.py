from django.conf.urls import url
from .views import project_views

app_name = 'opreport'

urlpatterns = [
        url(r'^$', project_views.index, name='index'),
        url(r'^input_data/$', project_views.input_data, name='input_data'),
    ]
