from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Users(models.Model):
    userid = models.ForeignKey(User, unique=True)
    username = models.CharField(max_length=30, unique=True)
    location = models.CharField(max_length=30)
    createTime = models.DateTimeField()
    lastLogin = models.DateTimeField()
    lastToken = models.CharField(max_length=32)
