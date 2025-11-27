from django.shortcuts import render
from .models import *


def home(request):
    studenti = Studenti.objects.all()
    return render(request, 'main/index.html', {"studenti":studenti})

def contatti(request):
    return render(request, 'main/contatti.html')
    
def chisiamo(request):
    return render(request, 'main/chi_siamo.html')


