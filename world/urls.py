from django.urls import path
from .views import *

urlpatterns = [
    path('world_home/', world_home, name="world_home"),
    path('add_dark_heresy/', add_dark_heresy, name="add_dark_heresy"),
    path(r'edit_dark_heresy/<int:pk>', edit_dark_heresy, name="edit_dark_heresy"),
    path(r'delete_dark_heresy/<int:pk>', delete_dark_heresy, name="delete_dark_heresy"),
    path(r'single_dark_heresy/<int:pk>', single_dark_heresy, name="single_dark_heresy"),
]