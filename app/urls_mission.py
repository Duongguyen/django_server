from django.urls import path
from . import views_intro_mission

urlpatterns = [
    path('', views_intro_mission.mission, name="mission"),
    path('create/', views_intro_mission.create, name="create_mission"),
    path('list/', views_intro_mission.list, name="list_mission"),
    path('edit/', views_intro_mission.update, name="edit_mission"),
    path('update/<str:id>', views_intro_mission.update, name="update_mission"),
]