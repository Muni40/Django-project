from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register("salle", SalleViewset)
router.register("utilisateur", UtilisateurViewset)
router.register("reservation", ReservationViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
]
