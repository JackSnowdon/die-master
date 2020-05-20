from django.shortcuts import render

# Create your views here.

def game_index(request):
    return render(request, "game_index.html")