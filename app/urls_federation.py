from django.urls import path
from . import views_intro_federation

urlpatterns = [
    path('', views_intro_federation.federation, name="federation"),
    path('create/', views_intro_federation.create, name="create_federation"),
    path('list/', views_intro_federation.list, name="list_federation"),
    path('edit/', views_intro_federation.update, name="edit_federation"),
    path('update/<str:id>', views_intro_federation.update, name="update_federation"),
]
