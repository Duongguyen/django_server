from django.urls import path
from . import views_competition

urlpatterns = [
    path('list/', views_competition.list, name="list_competition"),
    path('edit/', views_competition.update, name="edit_competition"),
    path('update/<str:id>', views_competition.update, name="update_competition"),
]