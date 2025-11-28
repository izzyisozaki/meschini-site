from django.shortcuts import render
from .models import *

# def home(request):
#     studenti = Studenti.objects.all()
#     return render(request, 'main/index.html', {"studenti":studenti})

def contatti(request):
    return render(request, 'main/contatti.html')

def areaAziende(request):
    return render(request, 'main/area-aziende.html')
    
def areaCandidati(request):
    return render(request, 'main/area-candidati.html')

def offerte(request):
    return render(request,'main/offerte-di-lavoro.html')


