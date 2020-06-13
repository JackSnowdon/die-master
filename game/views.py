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
            this_sheet.current_fate_points = this_sheet.max_fate_points
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
def send_dark_die_roll(request, pk, targetpk):
    this_game = get_object_or_404(DarkHeresyGame, pk=pk)
    target = get_object_or_404(DarkHeresyBase, pk=targetpk)
    profile = request.user.profile
    if profile == this_game.dm:
        if request.method == "POST":
            mod = int(request.POST.get("mod"))
            rolltype = request.POST.get("rolltype")
            die_form = DarkRollForm()
            form = die_form.save(commit=False)
            form.target_id = target.id
            form.roll_type = rolltype
            form.roll_game = this_game
            form.mod = mod
            form.fate_points = target.current_fate_points
            form.save()
            target.die_roll = get_object_or_404(DarkDieRoll, pk=form.id)
            target.save()
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )        
    return redirect("set_up_dark", this_game.id)


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
    if request.method == "POST":
        roll_form = DarkRollRoller(request.POST, instance=this_roll)
        if roll_form.is_valid():
            form = roll_form.save(commit=False)
            mod = form.mod
            total_thresh = form.threshold + mod
            if mod == 0:
                if form.roll_amount <= total_thresh:
                    form.passed = True
                    messages.error(
                        request, f"{this_roll.roll_type} Passed!", extra_tags="alert"
                    )
                else:
                    messages.error(
                        request, f"{this_roll.roll_type} Failed!", extra_tags="alert"
                    )
            else:
                if form.roll_amount <= total_thresh:
                    form.passed = True
                    messages.error(
                        request, f"{this_roll.roll_type} Passed! (+{mod} mod)", extra_tags="alert"
                    )
                elif form.roll_amount <= form.threshold:
                    messages.error(
                        request, f"{this_roll.roll_type} Failed Due To {mod} Modifer!", extra_tags="alert"
                    )
                else:
                    messages.error(
                        request, f"{this_roll.roll_type} Failed!", extra_tags="alert"
                    )
            roller.current_fate_points = form.fate_points
            roller.save()
            form.save()
            return redirect("set_up_dark", this_roll.roll_game.id)    
    else: 
        roll_form = DarkRollRoller(instance=this_roll)
        return render(request, "dark_die_roll.html", {"this_roll": this_roll, "roller": roller, "rolltype": rolltype, "roll_form": roll_form})


@login_required
def delete_all_done_dark_rolls(request, pk):
    this_game = get_object_or_404(DarkHeresyGame, pk=pk)
    profile = request.user.profile
    if profile == this_game.dm:
        rolls = this_game.all_game_rolls.all()
        for r in rolls:
            if r.roll_amount != 0 or r.passed:
                r.delete()
        messages.error(
            request, "All Completed Rolls Deleted", extra_tags="alert"
        )
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
    return redirect("set_up_dark", this_game.id)


@login_required
def delete_all_dark_rolls(request, pk):
    this_game = get_object_or_404(DarkHeresyGame, pk=pk)
    profile = request.user.profile
    if profile == this_game.dm:
        rolls = this_game.all_game_rolls.all()
        for r in rolls:
            r.delete()
        messages.error(
            request, "All Rolls Deleted", extra_tags="alert"
        )
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
    return redirect("set_up_dark", this_game.id)


@login_required
def send_all_dark_roll(request, pk):
    this_game = get_object_or_404(DarkHeresyGame, pk=pk)
    profile = request.user.profile
    if profile == this_game.dm:
        if request.method == "POST":
            sheets = this_game.sheets.all()
            mod = int(request.POST.get("mod"))
            rolltype = request.POST.get("rolltype")
            for sheet in sheets:
                die_form = DarkRollForm()
                form = die_form.save(commit=False)
                form.target_id = sheet.id
                form.roll_type = rolltype
                form.roll_game = this_game
                form.mod = mod
                form.fate_points = sheet.current_fate_points
                form.save()
                sheet.die_roll = get_object_or_404(DarkDieRoll, pk=form.id)
                sheet.save()
            messages.error(
                request, f"{rolltype} {mod} sent to all players", extra_tags="alert"
            )
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
    return redirect("set_up_dark", this_game.id)