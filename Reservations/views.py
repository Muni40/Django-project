from django.shortcuts import render 
from rest_framework import viewsets
from .models import *
from .serializers import *
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
def home(request):
    return render(request, template_name="reservations.html")
# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())
class SalleViewset(viewsets.ModelViewSet):
    queryset= Salle.objects.all()
    serializer_class = SalleSerializer

class UtilisateurViewset(viewsets.ModelViewSet):
    queryset= Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class ReservationViewset(viewsets.ModelViewSet):
    queryset= Reservation.objects.all()
    serializer_class = ReservationSerializer

# Create your views here.
