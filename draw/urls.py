# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('join/', views.join, name='join'),
    path('start/', views.start, name='start'),
    path('create1/', views.create1, name='create1'),
    path('create2/', views.create2, name='create2'),
    path('drawing1/', views.drawing1, name='drawing1'),
    path('drawing2/', views.drawing2, name='drawing2'),
    path('drawing3/', views.drawing3, name='drawing3'),
    path('next_team/', views.next_team, name='next_team'),
    path('last_team/', views.last_team, name='last_team'),
    path('score/', views.score, name='score'),
    path('home_phone/', views.home_phone, name='home_phone'),
    path('instruction/', views.instruction, name='instruction'),
    path('instructions_phone/', views.instructions_phone, name='instructions_phone'),
    path('instructions_phone_slide/', views.instructions_phone_slide, name='instructions_phone_slide'),
    path('start_phone/', views.start_phone, name='start_phone'),
    path('join_phone/', views.join_phone, name='join_phone'),
    path('num_players_phone/', views.num_players_phone, name='num_players_phone'),
    path('num_teams_phone/', views.num_teams_phone, name='num_teams_phone'),
    path('word/', views.word, name='word'),
    path('word_phone/', views.word_phone, name='word_phone'),
    path('drawing_phone/', views.drawing_phone, name='drawing_phone'),
    path('next_team_phone/', views.next_team_phone, name='next_team_phone'),
    path('guess/', views.guess, name='guess'),
    path('guess_phone/', views.guess_phone, name='guess_phone'),
    path('score_phone/', views.score_phone, name='score_phone'),
]
