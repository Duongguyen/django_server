from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name=""),
    path('register/', views.register, name="register"),
    path('login/', views.loginA, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('users/', views.users, name="users"),
    path('edit/', views.update_user, name="edit"),
]

