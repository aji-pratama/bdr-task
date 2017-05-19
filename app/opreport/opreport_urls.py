from django.conf.urls import url
from .views import project_views, quotation_views, tender_views, delivery_views

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

        # Tender
        url(r'^tender/$', tender_views.index_tender, name='index_tender'),
        url(r'^input-tender/$', tender_views.input_tender, name='input_tender'),
        url(r'^delete-tender-(?P<pk>\d+)$', tender_views.delete_tender, name='delete_tender'),

        # PI & Delivery
        url(r'^delivery/$', delivery_views.index_delivery, name='index_delivery'),
        url(r'^input-delivery/$', delivery_views.input_delivery, name='input_delivery'),
        url(r'^delete-delivery-(?P<pk>\d+)$', delivery_views.delete_delivery, name='delete_delivery'),
    ]
