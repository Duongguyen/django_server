from django.urls import path
from . import views_text

urlpatterns = [
    path('', views_text.text_qp, name="text"),
    path('create/', views_text.create, name="create_text"),
    path('list/', views_text.list, name="list_text"),
    path('edit/', views_text.update, name="edit_text"),
    path('update/<str:id>', views_text.update, name="update_text"),
]