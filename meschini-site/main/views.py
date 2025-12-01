from django.shortcuts import render
from .models import *

# def home(request):
#     studenti = Studenti.objects.all()
#     return render(request, 'main/index.html', {"studenti":studenti})

def contatti(request):
    return render(request, 'main/contatti.html')

def area_aziende(request):
    return render(request, 'main/area-aziende.html')
    
def area_candidati(request):
    return render(request, 'main/area-candidati.html')

def offerte_di_lavoro(request):
    return render(request,'main/offerte-di-lavoro.html')


