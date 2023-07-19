from django.urls import path
from . import views_contact

urlpatterns = [
    path('', views_contact.contact, name="contact"),
    path('create/', views_contact.contact, name="create_contact"),
    path('list/', views_contact.contact, name="list_contact"),
    path('edit/', views_contact.contact, name="edit_contact"),
    path('update/<str:id>', views_contact.contact, name="update_contact"),
]