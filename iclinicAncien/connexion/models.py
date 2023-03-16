from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from validate_email import validate_email

from email_validator import validate_email, EmailNotValidError
from django.core.validators import RegexValidator


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    password = models.CharField(max_length=255)    

    username = None
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
