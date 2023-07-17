from django.urls import path
from . import views_referee

urlpatterns = [
    path('', views_referee.referee, name="referee"),
    path('create/', views_referee.create, name="create_referee"),
    path('list/', views_referee.list, name="list_referee"),
    path('edit/', views_referee.update, name="edit_referee"),
    path('update/<str:id>', views_referee.update, name="update_referee"),
]