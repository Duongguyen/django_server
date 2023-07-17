from django.urls import path
from . import views_intro_evolution

urlpatterns = [
    path('', views_intro_evolution.evolution, name="evolution"),
    path('create/', views_intro_evolution.create, name="create_evolution"),
    path('list/', views_intro_evolution.list, name="list_evolution"),
    path('edit/', views_intro_evolution.update, name="edit_evolution"),
    path('update/<str:id>', views_intro_evolution.update, name="update_evolution"),
]