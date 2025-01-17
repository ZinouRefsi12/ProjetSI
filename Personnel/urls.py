from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  
    path('personnel/', views.liste_personnel, name='personnel'),  
    path('employe/', views.employe, name='employe'),
     path('ajouteremploye/', views.ajouter_employe, name='ajouter_employe'),
    
] 
