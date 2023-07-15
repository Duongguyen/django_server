from django.urls import path
from . import views_partner

urlpatterns = [
    path('', views_partner.partner, name="partner"),
    path('create/', views_partner.create, name="create_partner"),
    path('list/', views_partner.list, name="list_partner"),
    path('edit/', views_partner.update, name="edit_partner"),
    path('update/<str:id>', views_partner.update, name="update_partner"),
]