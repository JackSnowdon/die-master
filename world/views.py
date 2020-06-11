from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required
def world_home(request):
    profile = request.user.profile
    dh = profile.dh_sheets.all()
    return render(request, "world_home.html", {"dh": dh})


@login_required
def add_dark_heresy(request):
    if request.method == "POST":
        dark_form = DarkBaseForm(request.POST)
        if dark_form.is_valid():
            form = dark_form.save(commit=False)
            user = request.user
            form.created_by = user.profile
            form.current_fate_points = form.max_fate_points
            form.save()
            messages.error(request, "Added {0}".format(form.name), extra_tags="alert")
            return redirect("world_home")
    else:
        dark_form = DarkBaseForm()
    return render(request, "add_dark_heresy.html", {"dark_form": dark_form}) 


@login_required
def edit_dark_heresy(request, pk):
    this_sheet = get_object_or_404(DarkHeresyBase, pk=pk)
    profile = request.user.profile
    if profile == this_sheet.created_by or profile.staff_access:
        if request.method == "POST":
            dark_form = DarkBaseForm(request.POST, instance=this_sheet)
            if dark_form.is_valid():
                form = dark_form.save(commit=False)
                form.current_fate_points = form.max_fate_points
                form.save()
                messages.error(
                    request, "Edited {0}".format(form.name), extra_tags="alert"
                )
                return redirect("world_home")
        else:
            dark_form = DarkBaseForm(instance=this_sheet)
        return render(
            request,
            "edit_dark_heresy.html",
            {"dark_form": dark_form, "this_sheet": this_sheet},
        )
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("world_home")


@login_required
def delete_dark_heresy(request, pk):
    this_sheet = get_object_or_404(DarkHeresyBase, pk=pk)
    profile = request.user.profile
    if profile == this_sheet.created_by or profile.staff_access:
        messages.error(request, 'Deleted {0}'.format(this_sheet.name), extra_tags='alert')
        this_sheet.delete()
        return redirect(reverse('world_home'))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("world_home") 


@login_required
def single_dark_heresy(request, pk):
    this_sheet = get_object_or_404(DarkHeresyBase, pk=pk)
    profile = request.user.profile
    if profile == this_sheet.created_by or profile.staff_access:
        return render(request, "single_dark_heresy.html", {"this_sheet": this_sheet})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("world_home") 