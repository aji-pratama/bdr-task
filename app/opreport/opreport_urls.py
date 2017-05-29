from django.conf.urls import url
from .views import project_views, quotation_views, tender_views, delivery_views, ticket_views, cashadv_views, budgeting_views

app_name = 'opreport'

urlpatterns = [
        # Project Number
        url(r'^project$', project_views.index_project, name='index_project'),
        url(r'^input-project/$', project_views.input_project, name='input_project'),
        url(r'^edit-project-(?P<pk>\d+)$', project_views.edit_project, name='edit_project'),
        url(r'^delete-project-(?P<pk>\d+)$', project_views.delete_project, name='delete_project'),

        # Quotation
        url(r'^quotation/$', quotation_views.index_quotation, name='index_quotation'),
        url(r'^input-quotation/$', quotation_views.input_quotation, name='input_quotation'),
        url(r'^edit-quotation-(?P<pk>\d+)$', quotation_views.edit_quotation, name='edit_quotation'),
        url(r'^delete-quotation-(?P<pk>\d+)$', quotation_views.delete_quotation, name='delete_quotation'),

        # Tender
        url(r'^tender/$', tender_views.index_tender, name='index_tender'),
        url(r'^input-tender/$', tender_views.input_tender, name='input_tender'),
        url(r'^edit-tender-(?P<pk>\d+)$', tender_views.edit_tender, name='edit_tender'),
        url(r'^delete-tender-(?P<pk>\d+)$', tender_views.delete_tender, name='delete_tender'),

        # PI & Delivery
        url(r'^delivery/$', delivery_views.index_delivery, name='index_delivery'),
        url(r'^input-delivery/$', delivery_views.input_delivery, name='input_delivery'),
        url(r'^delete-delivery-(?P<pk>\d+)$', delivery_views.delete_delivery, name='delete_delivery'),

        # Cash Advance Ticket Project
        url(r'^ticket/$', ticket_views.index_ticket, name='index_ticket'),
        url(r'^input-ticket/$', ticket_views.input_ticket, name='input_ticket'),
        url(r'^delete-ticket-(?P<pk>\d+)$', ticket_views.delete_ticket, name='delete_ticket'),

        # Cash Advance Cashadv Project
        url(r'^cashadv/$', cashadv_views.index_cashadv, name='index_cashadv'),
        url(r'^input-cashadv/$', cashadv_views.input_cashadv, name='input_cashadv'),
        url(r'^delete-cashadv-(?P<pk>\d+)$', cashadv_views.delete_cashadv, name='delete_cashadv'),

        # BUDGETING
        url(r'^budgeting/$', budgeting_views.index_budgeting, name='index_budgeting'),
        url(r'^input-budgeting/$', budgeting_views.input_budgeting, name='input_budgeting'),
        url(r'^delete-budgeting-(?P<pk>\d+)$', budgeting_views.delete_budgeting, name='delete_budgeting'),
        # url(r'^budgeting-realisasi-(?P<pk>\d+)$', budgeting_views.budgeting_realisasi, name='budgeting_realisasi'),
    ]
