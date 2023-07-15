from django.urls import path
from . import views_event

urlpatterns = [
    path('', views_event.event, name="event"),
    path('create/', views_event.create, name="create_event"),
    path('list/', views_event.list, name="list_event"),
    path('edit/', views_event.update, name="edit_event"),
    path('update/<str:id>', views_event.update, name="update_event"),
]