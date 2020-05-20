from django.urls import path
from .views import *

urlpatterns = [
    path('game_index/', game_index, name="game_index"),
]