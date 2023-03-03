from django.contrib import admin
from .models import Patient, Medecin, Fonction, Profession, Etablissement


admin.site.register(Fonction)
admin.site.register(Profession)

admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Etablissement)
