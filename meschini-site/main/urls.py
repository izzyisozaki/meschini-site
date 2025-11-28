from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("contatti", views.contatti),
    path("chisiamo", views.chisiamo),
    path("offertelavoro", views.offerte_lavoro),

]