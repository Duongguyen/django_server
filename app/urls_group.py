from django.urls import path
from . import views_group

urlpatterns = [
    path('', views_group.group, name="group"),
    path('create/', views_group.create, name="create_group"),
    path('list/', views_group.list, name="list_group"),
    path('edit/', views_group.update, name="edit_group"),
    path('update/<str:id>', views_group.update, name="update_group"),
]