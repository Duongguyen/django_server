from django.urls import path
from . import views_blog

urlpatterns = [
    path('', views_blog.blog, name="blog"),
    path('create/', views_blog.save_blog, name="create_blog"),
    path('list/', views_blog.tables, name="list_blog"),
    path('edit/', views_blog.update_blog, name="edit_blog"),
    path('update/<str:id>', views_blog.update_blog, name="update_blog"),
]