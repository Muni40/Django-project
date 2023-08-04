from rest_framework import serializers
from .models import *

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = "__all__"

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
         model = Utilisateur
         fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__" 
        read_only_fields = "Utilisateur",   
        depth = 1       