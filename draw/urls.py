# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('join/', views.join, name='join'),
    path('start/', views.start, name='start')
]
