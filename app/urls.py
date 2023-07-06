from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('register/', views.register, name="register"),
    path('login/', views.loginA, name="login"),
]