from django.urls import path
from . import views_law

urlpatterns = [
    path('', views_law.law, name="law"),
    path('create/', views_law.create, name="create_law"),
    path('list/', views_law.list, name="list_law"),
    path('edit/', views_law.update, name="edit_law"),
    path('update/<str:id>', views_law.update, name="update_law"),
]