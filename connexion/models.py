from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from validate_email import validate_email
 
class User(AbstractUser):
    #username = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    
    password = models.CharField(max_length=255)    

    username = None
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

