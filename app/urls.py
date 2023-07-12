from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name=""),
    path('register/', views.register, name="register"),
    path('login/', views.loginA, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('input/', views.blog, name="input"),
    path('tables/', views.tables, name="tables"),
    path('photo/', views.photo, name="photo"),
    path('table/', views.table, name="table"),
    path('save/', views.save_blog, name="save"),
    path('submit/', views.save_photo, name="submit"),
    path('users/', views.users, name="users"),
]
