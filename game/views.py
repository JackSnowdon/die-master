from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from world.models import *

# Create your views here.

@login_required
def game_index(request):
    dark_sheets = DarkHeresyGame.objects.order_by('name')
    return render(request, "game_index.html", {"dark_sheets":dark_sheets })


@login_required
def start_new_dark_game(request):
    if request.method == "POST":
        game_form = DarkGameForm(request.POST)
        if game_form.is_valid():
            form = game_form.save(commit=False)
            form.dm = request.user.profile
            form.save()
            messages.error(request, "Started {0}".format(form.name), extra_tags="alert")
            return redirect("set_up_dark", form.id)
    else:
        game_form = DarkGameForm()
    return render(request, "start_new_dark_game.html", {"game_form": game_form}) 


@login_required
def set_up_dark(request, pk):
    this_game = get_object_or_404(DarkHeresyGame, pk=pk)
    dh_sheets = DarkHeresyBase.objects.order_by('name').filter(current_game=None)
    return render(request, "set_up_dark.html", {"this_game": this_game, "dh_sheets": dh_sheets})


@login_required
def change_dark_player_status(request, pk, gamepk):
    this_sheet = get_object_or_404(DarkHeresyBase, pk=pk)
    this_game = get_object_or_404(DarkHeresyGame, pk=gamepk)
    profile = request.user.profile
    if profile == this_game.dm or this_sheet.created_by == profile: 
        if this_sheet.current_game == None:
            this_sheet.current_game = this_game
            messages.error(request, 'Added {0} to {1}'.format(this_sheet.name, this_game.name), extra_tags='alert')
        else:
            this_sheet.current_game = None
            messages.error(request, 'Removed {0} from {1}'.format(this_sheet.name, this_game.name), extra_tags='alert')
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
    this_sheet.save()
    return redirect("set_up_dark", this_game.id)


@login_required
def change_ready_state(request, pk):
    this_game = get_object_or_404(DarkHeresyGame, pk=pk)
    profile = request.user.profile
    if profile == this_game.dm:
        if this_game.ready_state == False:
            this_game.ready_state = True
            messages.error(request, 'Set {0} to Ready'.format(this_game.name), extra_tags='alert')
        else:
            this_game.ready_state = False
            messages.error(request, 'Unreadied {0}'.format(this_game.name), extra_tags='alert')
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
    this_game.save()
    return redirect("set_up_dark", this_game.id)


@login_required
def delete_dark_heresy_game(request, pk):
    this_game = get_object_or_404(DarkHeresyGame, pk=pk)
    profile = request.user.profile
    if profile == this_game.dm or profile.staff_access:
        messages.error(request, 'Deleted {0}'.format(this_game.name), extra_tags='alert')
        this_game.delete()
        return redirect(reverse('game_index'))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("game_index")


@login_required
def send_dark_die_roll(request, gamepk, targetpk, rolltype):
    profile = request.user.profile
    this_game = get_object_or_404(DarkHeresyGame, pk=gamepk)
    target = get_object_or_404(DarkHeresyBase, pk=targetpk)
    if profile == this_game.dm:
        die_form = DarkRollForm()
        form = die_form.save(commit=False)
        form.target_id = target.id
        form.roll_type = rolltype
        form.roll_game = this_game
        form.save()
        target.die_roll = get_object_or_404(DarkDieRoll, pk=form.id)
        target.save()         
        return redirect("set_up_dark", this_game.id)
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("game_index")


@login_required
def delete_dark_die_roll(request, diepk):
    this_roll = get_object_or_404(DarkDieRoll, pk=diepk)
    profile = request.user.profile
    if profile == this_roll.roll_game.dm:
        messages.error(request, 'Deleted {0}'.format(this_roll.roll_type), extra_tags='alert')
        this_roll.delete()
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
    return redirect("set_up_dark", this_roll.roll_game.id)


@login_required
def dark_die_roll(request, diepk):
    this_roll = get_object_or_404(DarkDieRoll, pk=diepk)
    roller = get_object_or_404(DarkHeresyBase, pk=this_roll.target_id)
    rolltype = this_roll.roll_type.replace(" ", "_").lower() 
    return render(request, "dark_die_roll.html", {"this_roll": this_roll, "roller": roller, "rolltype": rolltype})


@login_required
def dark_die_result(request, diepk, result):
    this_roll = get_object_or_404(DarkDieRoll, pk=diepk)
    roller = get_object_or_404(DarkHeresyBase, pk=this_roll.target_id)
    if result == 1:
        this_roll.passed = True
    this_roll.save()
    return redirect("set_up_dark", this_roll.roll_game.id)

    