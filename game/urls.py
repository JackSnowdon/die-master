from django.urls import path
from .views import *

urlpatterns = [
    path('game_index/', game_index, name="game_index"),
    path('start_new_dark_game/', start_new_dark_game, name="start_new_dark_game"),
    path(r'set_up_dark/<int:pk>', set_up_dark, name="set_up_dark"),
    path(r'delete_dark_heresy_game/<int:pk>', delete_dark_heresy_game, name="delete_dark_heresy_game"),
    path(r'change_dark_player_status/<int:pk>/<int:gamepk>', change_dark_player_status, name="change_dark_player_status"),
    path(r'change_ready_state/<int:pk>', change_ready_state, name="change_ready_state"),
    path(r'send_dark_die_roll/<int:gamepk>/<int:targetpk>/<str:rolltype>', send_dark_die_roll, name="send_dark_die_roll"),
    path(r'delete_dark_die_roll/<int:diepk>', delete_dark_die_roll, name="delete_dark_die_roll"),
    path(r'dark_die_roll/<int:diepk>', dark_die_roll, name="dark_die_roll"),
    path(r'dark_die_result/<int:diepk>/<int:result>', dark_die_result, name="dark_die_result"),
]