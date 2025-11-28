from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("contatti", views.contatti),
    path("area-aziende", views.area_aziende),
    path("area-candidati", views.area_candidati)
    path("offerte-di-lavoro", views.offerte_di_lavoro),

]