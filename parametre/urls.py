from django.urls import path
from rest_framework import routers

from parametre.views import PatientViewSet, MedecinViewSet, EtablissementViewSet

router = routers.DefaultRouter()
router.register('patient', PatientViewSet)
router.register('medecin', MedecinViewSet)
router.register('etablissement', EtablissementViewSet)

app_name="parametre"
urlpatterns = [

]