from django.urls import path
from .views import *

urlpatterns = [
    path('game_index/', game_index, name="game_index"),
    path('start_new_dark_game/', start_new_dark_game, name="start_new_dark_game"),
    path(r'set_up_dark/<int:pk>', set_up_dark, name="set_up_dark"),
    path(r'delete_dark_heresy_game/<int:pk>', delete_dark_heresy_game, name="delete_dark_heresy_game"),
    path(r'change_dark_player_status/<int:pk>/<int:gamepk>', change_dark_player_status, name="change_dark_player_status"),
    path(r'change_ready_state/<int:pk>', change_ready_state, name="change_ready_state"),
    path(r'send_dark_die_roll/<int:pk>/<int:targetpk>', send_dark_die_roll, name="send_dark_die_roll"),
    path(r'delete_dark_die_roll/<int:diepk>', delete_dark_die_roll, name="delete_dark_die_roll"),
    path(r'dark_die_roll/<int:diepk>', dark_die_roll, name="dark_die_roll"),
    path(r'delete_all_done_dark_rolls/<int:pk>', delete_all_done_dark_rolls, name="delete_all_done_dark_rolls"),
    path(r'delete_all_dark_rolls/<int:pk>', delete_all_dark_rolls, name="delete_all_dark_rolls"),
    path(r'send_all_dark_roll/<int:pk>', send_all_dark_roll, name="send_all_dark_roll"),
    path(r'reset_all_fate_points/<int:pk>', reset_all_fate_points, name="reset_all_fate_points"),
    path(r'reward_fate_point/<int:pk>/<int:targetpk>', reward_fate_point, name="reward_fate_point"),
    path(r'init_combat/<int:pk>', init_combat, name="init_combat"),
    path(r'enter_combat/<int:combatpk>', enter_combat, name="enter_combat"),
    path(r'roll_dark_init/<int:pk>/', roll_dark_init, name="roll_dark_init"),
    path(r'delete_all_combats/<int:pk>/', delete_all_combats, name="delete_all_combats"),
]