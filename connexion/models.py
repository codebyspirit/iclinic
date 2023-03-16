from datetime import datetime, timedelta
from django.utils import timezone
from django.apps import apps
from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
import jwt
from django.conf import settings

from email_validator import validate_email, EmailNotValidError
# Create your models 
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

def verifier():
    try:
        v = validate_email('kreadou@gmail')
        email = v["email"] 
    except EmailNotValidError as e:
        print(str(e))

verifier()


class MyUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError("The given username must be set")
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), blank=False, unique=True,
        validators=[RegexValidator(
        r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
        'Entrez une adresse e-mail valide',
        'Invalid'
        )])

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    email_verified = models.BooleanField(_("email_verified"), default=False,
                                         help_text=_(
                                             "Designates whether this user email is verified."
                                         ),
                                         )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    objects = MyUserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def token(self):
        return jwt.encode(
            {"username": self.username, "email": self.email, "exp": datetime.utcnow() + timedelta(hours=24)},
            settings.SECRET_KEY, 'HS256')

    """
    def clean(self):
        if not verifier():
            raise ValidationError('incorret email')
    """
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)