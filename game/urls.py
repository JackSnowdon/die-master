from django.urls import path
from .views import *

urlpatterns = [
    path('game_index/', game_index, name="game_index"),
    path('start_new_dark_game/', start_new_dark_game, name="start_new_dark_game"),
    path(r'set_up_dark/<int:pk>', set_up_dark, name="set_up_dark"),
    path(r'delete_dark_heresy_game/<int:pk>', delete_dark_heresy_game, name="delete_dark_heresy_game"),
    path(r'change_dark_player_status/<int:pk>/<int:gamepk>', change_dark_player_status, name="change_dark_player_status"),
    
]