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

def drawing(request):
    return render(request, 'draw/drawing.html')

def next_team(request):
    return render(request, 'draw/next_team.html')

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

def home_t1(request):
    return render(request, 'draw/home_t1.html')

def home_t2(request):
    return render(request, 'draw/home_t2.html')

def home_t3(request):
    return render(request, 'draw/home_t3.html')

def instruction(request):
    return render(request, 'draw/instruction.html')

def instructions_t1(request):
    return render(request, 'draw/instructions_t1.html')

def instructions_t2(request):
    return render(request, 'draw/instructions_t2.html')

def instructions_t3(request):
    return render(request, 'draw/instructions_t3.html')

def start_t1(request):
    return render(request, 'draw/start_t1.html')

def start_t2(request):
    return render(request, 'draw/start_t2.html')

def start_t3(request):
    return render(request, 'draw/start_t3.html')

def join_t1(request):
    return render(request, 'draw/join_t1.html')

def join_t2(request):
    return render(request, 'draw/join_t2.html')

def join_t3(request):
    return render(request, 'draw/join_t3.html')

def num_players_t1(request):
    return render(request, 'draw/num_players_t1.html')

def num_players_t2(request):
    return render(request, 'draw/num_players_t2.html')

def num_players_t3(request):
    return render(request, 'draw/num_players_t3.html')

def num_teams_t1(request):
    return render(request, 'draw/num_teams_t1.html')

def num_teams_t2(request):
    return render(request, 'draw/num_teams_t2.html')

def num_teams_t3(request):
    return render(request, 'draw/num_teams_t3.html')

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

def score_t1_phone(request):
    return render(request, 'draw/score_t1_phone.html')

def score_t2_phone(request):
    return render(request, 'draw/score_t2_phone.html')

def score_t3_phone(request):
    return render(request, 'draw/score_t3_phone.html')
