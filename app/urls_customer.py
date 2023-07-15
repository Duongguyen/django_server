from django.urls import path
from . import views_customer

urlpatterns = [
    path('', views_customer.customer, name="customer"),
    path('create/', views_customer.save_customer, name="create_customer"),
    path('list/', views_customer.customer_tables, name="list_customer"),
    path('edit/', views_customer.update_customer, name="edit_customer"),
    path('update/<str:id>', views_customer.update_customer, name="update_customer")
]
