from django.conf.urls import url
from . import views

app_name = 'budgeting'

urlpatterns = [
        # Budgeting
        url(r'^add-budgeting$', views.BudgetingCreate.as_view(), name='create_budgeting')
    ]
