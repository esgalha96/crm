#acesso/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    phone_number = models.CharField(verbose_name="Celular", max_length=11, blank=False, null=None)
