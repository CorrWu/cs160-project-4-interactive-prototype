# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')
    
def home(request):
    return render(request, 'draw/home.html')

def join(request):
    return render(request, 'draw/join.html')

def start(request):
    return render(request, 'draw/start.html')

def create1(request):
    return render(request, 'draw/create1.html')

def create2(request):
    return render(request, 'draw/create2.html')

def home_phone(request):
    return render(request, 'draw/home_phone.html')

def instruction(request):
    return render(request, 'draw/instruction.html')

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

def word(request):
    return render(request, 'draw/word.html')

def word_phone(request):
    return render(request, 'draw/word_phone.html')

def drawing_phone(request):
    return render(request, 'draw/drawing_phone.html')

def next_team_phone(request):
    return render(request, 'draw/next_team_phone.html')

def guess(request):
    return render(request, 'draw/guess.html')

def guess_phone(request):
    return render(request, 'draw/guess_phone.html')

def score_phone(request):
    return render(request, 'draw/score_phone.html')


