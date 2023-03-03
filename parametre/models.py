from django.db import models
from django.utils import timezone




CIVILITES = (
    ('Monsieur', 'M.'),
    ('Madame', 'Mme'),
    ('Mademoiselle', 'Mlle'),
  )  
SEXES = (
    ('M', 'Masculin'), 
    ('F', 'Féminin')
)



class Fonction(models.Model):
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    
    class Meta:
        ordering=('libelle',)

    def __str__(self):
        return "{0}".format(self.libelle)


class Profession(models.Model):
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    
    class Meta:
        ordering=('libelle',)
    
    def __str__(self):
        return "{0}".format(self.libelle)


class Patient(models.Model):
    matricule = models.CharField(max_length=15, unique=True, verbose_name="matricule")
    civilite = models.CharField(max_length=20, choices=CIVILITES, blank=True, verbose_name="civilité")
    nom = models.CharField(max_length=50, verbose_name="nom")
    prenoms = models.CharField(max_length=100, verbose_name="prenoms")
    fonction = models.ForeignKey(Fonction,  on_delete=models.CASCADE, verbose_name="fonction")
    profession = models.ForeignKey(Profession,  on_delete=models.CASCADE, verbose_name="profession")
    telephone = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="téléphone")
    cellulaire = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="cellulaire")
    email = models.CharField(max_length=100, default="", blank=True, null=True, verbose_name="e-mail")
    sexe = models.CharField(max_length=1, choices=SEXES, default='M', verbose_name="sexe")
    photo = models.ImageField(upload_to='users', blank=True, null=True, verbose_name="photo")
    
    def __str__(self):
        return "{0}, {1}".format(self.nom.upper(), self.prenoms.title())


class Medecin(models.Model):
    matricule = models.CharField(max_length=15, unique=True, verbose_name="matricule")
    civilite = models.CharField(max_length=20, choices=CIVILITES, blank=True, verbose_name="civilité")
    nom = models.CharField(max_length=50, verbose_name="nom")
    prenoms = models.CharField(max_length=100, verbose_name="prenoms")
    fonction = models.ForeignKey(Fonction,  on_delete=models.CASCADE, verbose_name="fonction")
    profession = models.ForeignKey(Profession,  on_delete=models.CASCADE, verbose_name="profession")
    telephone = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="téléphone")
    cellulaire = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="cellulaire")
    email = models.CharField(max_length=100, default="", blank=True, null=True, verbose_name="e-mail")
    sexe = models.CharField(max_length=1, choices=SEXES, default='M', verbose_name="sexe")
    photo = models.ImageField(upload_to='users', blank=True, null=True, verbose_name="photo")
    
    def __str__(self):
        return "{0}, {1}".format(self.nom.upper(), self.prenoms.title())


class Etablissement(models.Model):
    raisonSociale = models.CharField(max_length=255, unique=True, verbose_name="raison sociale")
    sigle = models.CharField(max_length=50, default="", blank=True, null=True, verbose_name="sigle")
    telephone = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="téléphone")
    cellulaire = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="cellulaire")
    email = models.EmailField(default="", blank=True, null=True, verbose_name="e-mail")
    dateCreation = models.DateField(default=timezone.now, blank=True, null=True, verbose_name="date envoi des email")
    historique = models.TextField(default="", blank=True, null=True, verbose_name="historique")
    logo = models.ImageField(upload_to='images', default="", blank=True, null=True, verbose_name="logo")
    photo = models.ImageField(upload_to='images', default="", blank=True, null=True, verbose_name="photo")
     
    def __str__(self):
        return "{0}".format(self.raisonSociale)


