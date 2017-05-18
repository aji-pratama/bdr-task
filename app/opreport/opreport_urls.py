from django.conf.urls import url
from .views import project_views, quotation_views

app_name = 'opreport'

urlpatterns = [
        # Project Number
        url(r'^project$', project_views.index_project, name='index_project'),
        url(r'^input-project/$', project_views.input_project, name='input_project'),
        url(r'^delete-project-(?P<pk>\d+)$', project_views.delete_project, name='delete_project'),

        # Quotation
        url(r'^quotation/$', quotation_views.index_quotation, name='index_quotation'),
        url(r'^input-quotation/$', quotation_views.input_quotation, name='input_quotation'),
        url(r'^delete-quotation-(?P<pk>\d+)$', quotation_views.delete_quotation, name='delete_quotation'),
    ]
