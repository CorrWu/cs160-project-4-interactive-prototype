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

def drawing1(request):
    return render(request, 'draw/drawing1.html')

def drawing2(request):
    return render(request, 'draw/drawing2.html')

def drawing3(request):
    return render(request, 'draw/drawing3.html')

def next_team(request):
    return render(request, 'draw/next_team.html')

def next_team_t2(request):
    return render(request, 'draw/next_team_t2.html')

def next_team_t3(request):
    return render(request, 'draw/next_team_t3.html')

def times_up_t1(request):
    return render(request, 'draw/times_up_t1.html')

def times_up_t2(request):
    return render(request, 'draw/times_up_t2.html')

def times_up_t3(request):
    return render(request, 'draw/times_up_t3.html')

def t1_t2(request):
    return render(request, 'draw/t1_t2.html')

def t1_t3(request):
    return render(request, 'draw/t1_t3.html')

def t2_t1(request):
    return render(request, 'draw/t2_t1.html')

def t2_t3(request):
    return render(request, 'draw/t2_t3.html')

def t3_t1(request):
    return render(request, 'draw/t3_t1.html')

def t3_t2(request):
    return render(request, 'draw/t3_t2.html')

def t2_turn(request):
    return render(request, 'draw/t2_turn.html')

def t3_turn(request):
    return render(request, 'draw/t3_turn.html')

def next_t3_t1(request):
    return render(request, 'draw/next_t3_t1.html')

def next_t2_t3(request):
    return render(request, 'draw/next_t2_t3.html')

def t1_vote(request):
    return render(request, 'draw/t1_vote.html')

def t2_vote(request):
    return render(request, 'draw/t2_vote.html')

def last_team(request):
    return render(request, 'draw/last_team.html')

def score(request):
    return render(request, 'draw/score.html')

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

def word_t1_phone(request):
    return render(request, 'draw/word_t1_phone.html')

def word_t2_phone(request):
    return render(request, 'draw/word_t2_phone.html')

def word_t3_phone(request):
    return render(request, 'draw/word_t3_phone.html')

def drawing_t1_phone(request):
    return render(request, 'draw/drawing_t1_phone.html')

def drawing_t2_phone(request):
    return render(request, 'draw/drawing_t2_phone.html')

def drawing_t3_phone(request):
    return render(request, 'draw/drawing_t3_phone.html')

def guess(request):
    return render(request, 'draw/guess.html')

def t1_guess(request):
    return render(request, 'draw/t1_guess.html')

def t2_guess(request):
    return render(request, 'draw/t2_guess.html')

def t3_guess(request):
    return render(request, 'draw/t3_guess.html')

def score_phone(request):
    return render(request, 'draw/score_phone.html')

