from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    createTime = models.DateTimeField()
    lastLogin = models.DateTimeField()
    lastToken = models.CharField(max_length=32)
