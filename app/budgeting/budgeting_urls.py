from django.conf.urls import url
from . import views

app_name = 'budgeting'

urlpatterns = [
        # Budgeting
        url(r'^add-budgeting$', views.add_budgeting, name='create_budgeting'),
        url(r'^items-budgeting-(?P<pk>\d+)$', views.budgeting_items, name='budgeting_items'),

    ]
