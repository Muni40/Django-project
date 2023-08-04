from django.db import models
#import datetime
#from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Salle(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=80)
    place = models.PositiveIntegerField()
    superficie = models.PositiveIntegerField()
    equipement = models.CharField(max_length=500)
    prix = models.IntegerField()
    #localisation = 
    #mode_de_paiement= 

    #def __str__(self):
      # return f"{self.salle_reservee} - {self.utilisateur} "    

    class Meta:
       verbose_name_plural = "Salle"

class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=16)

    class Meta:
       verbose_name_plural = "Utilisateur"

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date= models.DateTimeField()
    salle_reservee = models.ForeignKey(Salle ,null=False, on_delete=models.PROTECT)
    utilisateur = models.ForeignKey(User, null=False , on_delete=models.PROTECT)


    class Meta():
       verbose_name_plural = "Reservation"

#class Panier(models.Model):


#class Categories(models.Model):

