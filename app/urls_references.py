from django.urls import path
from . import views_references

urlpatterns = [
    path('', views_references.reference, name="references"),
    path('create/', views_references.create, name="create_references"),
    path('list/', views_references.list, name="list_references"),
    path('edit/', views_references.update, name="edit_references"),
    path('update/<str:id>', views_references.update, name="update_references"),
]