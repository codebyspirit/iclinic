from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    #username = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)    

    username = None
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]