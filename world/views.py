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
            form.save()
            messages.error(request, "Added {0}".format(form.name), extra_tags="alert")
            return redirect("world_home")
    else:
        dark_form = DarkBaseForm()
    return render(request, "add_dark_heresy.html", {"dark_form": dark_form}) 