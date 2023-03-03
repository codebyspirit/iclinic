from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import PatientSerializer, MedecinSerializer, EtablissementSerializer 
from .models import Patient, Medecin, Etablissement




class PatientViewSet(viewsets.ModelViewSet):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer


class MedecinViewSet(viewsets.ModelViewSet):
	queryset = Medecin.objects.all()
	serializer_class = MedecinSerializer


class EtablissementViewSet(viewsets.ModelViewSet):
	queryset = Etablissement.objects.all()
	serializer_class = EtablissementSerializer



