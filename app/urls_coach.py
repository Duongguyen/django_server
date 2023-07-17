from django.urls import path
from . import views_coach

urlpatterns = [
    path('', views_coach.coach, name="coach"),
    path('create/', views_coach.create, name="create_coach"),
    path('list/', views_coach.list, name="list_coach"),
    path('edit/', views_coach.update, name="edit_coach"),
    path('update/<str:id>', views_coach.update, name="update_coach"),
]