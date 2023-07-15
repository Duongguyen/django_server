from django.urls import path
from . import views_photo

urlpatterns = [
    path('', views_photo.photo, name="photo"),
    path('create/', views_photo.save_photo, name="create_photo"),
    path('list/', views_photo.table, name="list_photo"),
    path('edit/', views_photo.update_photo, name="edit_photo"),
    path('update/<str:id>', views_photo.update_photo, name="update_photo"),
]
