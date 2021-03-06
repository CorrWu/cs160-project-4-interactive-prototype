# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home_t1/', views.home_t1, name='home_t1'),
    path('home_t2/', views.home_t2, name='home_t2'),
    path('home_t3/', views.home_t3, name='home_t3'),
    path('join/', views.join, name='join'),
    path('start/', views.start, name='start'),
    path('create1/', views.create1, name='create1'),
    path('create2/', views.create2, name='create2'),
    path('drawing/', views.drawing, name='drawing'),
    path('last_team/', views.last_team, name='last_team'),
    path('score/', views.score, name='score'),
    path('instruction/', views.instruction, name='instruction'),
    path('instructions_t1/', views.instructions_t1, name='instructions_t1'),
    path('instructions_t2/', views.instructions_t2, name='instructions_t2'),
    path('instructions_t3/', views.instructions_t3, name='instructions_t3'),
    path('start_t1/', views.start_t1, name='start_t1'),
    path('start_t2/', views.start_t2, name='start_t2'),
    path('start_t3/', views.start_t3, name='start_t3'),
    path('join_t1/', views.join_t1, name='join_t1'),
    path('join_t2/', views.join_t2, name='join_t2'),
    path('join_t3/', views.join_t3, name='join_t3'),
    path('num_players_t1/', views.num_players_t1, name='num_players_t1'),
    path('num_players_t2/', views.num_players_t2, name='num_players_t2'),
    path('num_players_t3/', views.num_players_t3, name='num_players_t3'),
    path('num_teams_t1/', views.num_teams_t1, name='num_teams_t1'),
    path('num_teams_t2/', views.num_teams_t2, name='num_teams_t2'),
    path('num_teams_t3/', views.num_teams_t3, name='num_teams_t3'),
    path('word/', views.word, name='word'),
    path('word_t1_phone/', views.word_t1_phone, name='word_t1_phone'),
    path('word_t2_phone/', views.word_t2_phone, name='word_t2_phone'),
    path('word_t3_phone/', views.word_t3_phone, name='word_t3_phone'),
    path('drawing_t1_phone/', views.drawing_t1_phone, name='drawing_t1_phone'),
    path('drawing_t2_phone/', views.drawing_t2_phone, name='drawing_t2_phone'),
    path('drawing_t3_phone/', views.drawing_t3_phone, name='drawing_t3_phone'),
    path('times_up_t1/', views.times_up_t1, name='times_up_t1'),
    path('times_up_t2/', views.times_up_t2, name='times_up_t2'),
    path('times_up_t3/', views.times_up_t3, name='times_up_t3'),
    path('t1_t2/', views.t1_t2, name='t1_t2'),
    path('t1_t3/', views.t1_t3, name='t1_t3'),
    path('t2_t1/', views.t2_t1, name='t2_t1'),
    path('t2_t3/', views.t2_t3, name='t2_t3'),
    path('t3_t1/', views.t3_t1, name='t3_t1'),
    path('t3_t2/', views.t3_t2, name='t3_t2'),
    path('t2_turn/', views.t2_turn, name='t2_turn'),
    path('t3_turn/', views.t3_turn, name='t3_turn'),
    path('next_t3_t1/', views.next_t3_t1, name='next_t3_t1'),
    path('next_t2_t3/', views.next_t2_t3, name='next_t2_t3'),
    path('t1_vote/', views.t1_vote, name='t1_vote'),
    path('t2_vote/', views.t2_vote, name='t2_vote'),
    path('guess/', views.guess, name='guess'),
    path('t1_guess/', views.t1_guess, name='t1_guess'),
    path('t2_guess/', views.t2_guess, name='t2_guess'),
    path('t3_guess/', views.t3_guess, name='t3_guess'),
    path('score_t1_phone/', views.score_t1_phone, name='score_t1_phone'),
    path('score_t2_phone/', views.score_t2_phone, name='score_t2_phone'),
    path('score_t3_phone/', views.score_t3_phone, name='score_t3_phone')
]
