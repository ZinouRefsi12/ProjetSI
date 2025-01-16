from django.db import models

from django.utils.timezone import now

# Create your models here.

class service(models.Model):
 nom= models.CharField(max_length=50)
 description= models.CharField(max_length=300)
 def __str__(self):
        return self.nom
 
class personnel(models.Model):

    nom = models.CharField(max_length=50)  
    prenom = models.CharField(max_length=50 )
    dateN = models.DateField(null=True, blank=True)  
    numT = models.FloatField(null=True, blank=True)  
    email = models.CharField(max_length=100)
    posteOccupe = models.CharField(max_length=50) 
    dateEmbauche = models.DateField(null=True, blank=True) 
    adresse = models.TextField(null=True, blank=True)
    serviceEmp = models.ForeignKey(service, on_delete=models.CASCADE, null=True, blank=True) 
    def __str__(self):
        return self.nom
    #Embuchement = models.ForeignKey(recrutement, on_delete=models.CASCADE)

class conges(models.Model):
 #dateD= models.DateField(null=True, blank=True)
 #dateF= models.DateField(null=True, blank=True)

 TYPE_CONGE_CHOICES = [    
        ('maternelle', 'Maternelle'),
        ('paternelle', 'Paternelle'),
        ('annuel', 'Annuel'),
        ('maladie', 'Maladie'),
    ]
 type_conge = models.CharField(
        max_length=50,  # Taille maximale
        choices=TYPE_CONGE_CHOICES,  # Valeurs autorisées
        default='annuel',  # Valeur par défaut
    )  
 Empconge = models.ForeignKey(personnel, on_delete=models.CASCADE)



class recrutement(models.Model):
    dateRec = models.DateField(null=True, blank=True)  # Autorise les valeurs nulles
    posteRecru = models.CharField(max_length=50,null=True, blank=True)
    statutrecrutement = models.CharField(max_length=50,null=True, blank=True)


class condidat(models.Model):
    nom = models.CharField(max_length=50,null=True, blank=True)
    prenom = models.CharField(max_length=50,null=True, blank=True)
    numT = models.FloatField(null=True, blank=True)  
    email = models.CharField(max_length=100,null=True, blank=True)  # Correction du nom
    statutCondidat = models.CharField(max_length=50,null=True, blank=True)
    statutCondidat = models.CharField(max_length=50,null=True, blank=True)
    recrutementCondidat = models.ForeignKey(recrutement, on_delete=models.CASCADE)
 
class Contrat(models.Model):
    type = models.CharField(max_length=50)
    dateD = models.DateField(null=True, blank=True)
    dateF = models.DateField(null=True, blank=True)
    salaire = models.FloatField(null=True, blank=True)  # Supprimez max_length
    contratEmp = models.ForeignKey(personnel, on_delete=models.CASCADE) 

class evaluation(models.Model):
    dateEv = models.DateField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)  # Supprimez max_length
    commentaire = models.CharField(max_length=300,null=True, blank=True)
    evalueremp = models.ForeignKey(personnel, on_delete=models.CASCADE)


class salaire(models.Model):
    salaireBase = models.FloatField(null=True, blank=True)  # Supprimez max_length
    Prime = models.FloatField(null=True, blank=True)
    heure_Sup = models.FloatField(null=True, blank=True)
    avance = models.FloatField(null=True, blank=True)
    jourAbsence = models.FloatField(null=True, blank=True)
    salaireF = models.FloatField(null=True, blank=True)
    SalaireEmp = models.ForeignKey(personnel, on_delete=models.CASCADE)


    