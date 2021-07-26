# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def home(request):
    return render(request, 'draw/home.html')

def home_phone(request):
    return render(request, 'draw/home_phone.html')

def instructions_phone(request):
    return render(request, 'draw/instructions_phone.html')

def instructions_phone_slide(request):
    return render(request, 'draw/instructions_phone_slide.html')

def start_phone(request):
    return render(request, 'draw/start_phone.html')

def join_phone(request):
    return render(request, 'draw/join_phone.html')

def num_players_phone(request):
    return render(request, 'draw/num_players_phone.html')

def num_teams_phone(request):
    return render(request, 'draw/num_teams_phone.html')


