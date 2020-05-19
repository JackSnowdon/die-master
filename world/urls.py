from django.urls import path
from .views import *

urlpatterns = [
    path('world_home/', world_home, name="world_home"),
    path('add_dark_heresy/', add_dark_heresy, name="add_dark_heresy")
]