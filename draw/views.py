# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')
    
def home(request):
    return render(request, 'draw/home.html')

def join(request):
    return render(request, 'draw/join.html')