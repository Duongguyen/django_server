from django.urls import path
from . import views_intro_greeting

urlpatterns = [
    path('', views_intro_greeting.greeting, name="greeting"),
    path('create/', views_intro_greeting.create, name="create_greeting"),
    path('list/', views_intro_greeting.list, name="list_greeting"),
    path('edit/', views_intro_greeting.update, name="edit_greeting"),
    path('update/<str:id>', views_intro_greeting.update, name="update_greeting"),
]