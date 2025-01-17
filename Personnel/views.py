from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import date
from .models import personnel, service


def home(request):
    return render(request, 'home.html')

def liste_personnel(request):  # Changer le nom pour éviter le conflit
    # ✅ Récupérer tous les employés avec leur service
    personnel_list = personnel.objects.select_related('serviceEmp').all()

    return render(request, 'personnel.html', {'personnel': personnel_list})

def employe(request):
    return render(request, 'employe.html')

def ajouter_employe(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        dateN = request.POST['dateN']
        numT = request.POST['numT']
        email = request.POST['email']
        posteOccupe = request.POST['posteOccupe']
        dateEmbauche = request.POST['dateEmbauche']
        adresse = request.POST['adresse']
        serviceEmp_nom = request.POST['serviceEmp']

        serviceEmp, created = service.objects.get_or_create(nom=serviceEmp_nom)
        personnel.objects.create(
            nom=nom,
            prenom=prenom,
            dateN=dateN,
            numT=numT,
            email=email,
            posteOccupe=posteOccupe,
            dateEmbauche=dateEmbauche,
            adresse=adresse,
            serviceEmp=serviceEmp
        )
        return redirect('personnel')
    return render(request, 'ajouteremploye.html')
