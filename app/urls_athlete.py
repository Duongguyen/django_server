from django.urls import path
from . import view_profile

urlpatterns = [
    path('', view_profile.athlete, name="athlete"),
    path('create/', view_profile.create, name="create_athlete"),
    path('list/', view_profile.list, name="list_athlete"),
    path('edit/', view_profile.update, name="edit_athlete"),
    path('update/<str:id>', view_profile.update, name="update_athlete"),
]