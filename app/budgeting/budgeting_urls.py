from django.conf.urls import url
from . import views

app_name = 'budgeting'

urlpatterns = [
        # Budgeting
        url(r'^add-budgeting$', views.add_budgeting, name='create_budgeting'),
        url(r'^items-budgeting-(?P<pk>\d+)$', views.budgeting_items, name='budgeting_items'),
        url(r'^get-items(?P<pk>\d+)$', views.get_items, name='get_items'),
        url(r'^delete-item(?P<pk>\d+)$', views.delete_item, name='delete_item')
    ]
