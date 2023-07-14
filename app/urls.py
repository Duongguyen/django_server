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
    path('edit/', views.update_user, name="edit"),
    path('customer/', views.customer, name="customer"),
    path('commit/', views.save_customer, name="commit"),
    path('push/', views.customer_tables, name="push"),
    path('edit_customer/', views.update_customer, name="edit_customer"),
    path('update/<str:id>', views.update_customer, name="update"),
]
