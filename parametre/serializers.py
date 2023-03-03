from rest_framework import serializers

from .models import Patient, Medecin, Etablissement


class EtablissementSerializer(serializers.Serializer):
    class Meta:
    	model = Etablissement
    	fields = '__all__'


class PatientSerializer(serializers.Serializer):
    class Meta:
    	model = Patient
    	fields = '__all__'


class MedecinSerializer(serializers.Serializer):
    class Meta:
    	model = Medecin
    	fields = '__all__'
