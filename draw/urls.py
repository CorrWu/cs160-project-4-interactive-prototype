# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('join/', views.join, name='join'),
    path('start/', views.start, name='start'),
    path('create1/', views.create1, name='create1'),
    path('home_phone/', views.home_phone, name='home_phone'),
    path('instruction/', views.instruction, name='instruction'),
    path('instructions_phone/', views.instructions_phone, name='instructions_phone'),
    path('instructions_phone_slide/', views.instructions_phone_slide, name='instructions_phone_slide'),
    path('start_phone/', views.start_phone, name='start_phone'),
    path('join_phone/', views.join_phone, name='join_phone'),
    path('num_players_phone/', views.num_players_phone, name='num_players_phone'),
    path('num_teams_phone/', views.num_teams_phone, name='num_teams_phone'),
]
