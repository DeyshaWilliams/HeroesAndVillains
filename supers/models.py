from ftplib import MAXLINE
import imp
from unittest.util import _MAX_LENGTH
from django.db import models
from super_types.models import Super_type

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(Super_type, on_delete=models.CASCADE, null=True)
