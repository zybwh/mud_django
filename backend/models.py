from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class UserStats(models.Model):
    currentHp = models.PositiveIntegerField(default=0)
    maxHp = models.PositiveIntegerField(default=0)
    currentMana = models.PositiveIntegerField(default=0)
    maxMana = models.PositiveIntegerField(default=0)
    power = models.PositiveIntegerField(default=0)
    agility = models.PositiveIntegerField(default=0)
    intelligent = models.PositiveIntegerField(default=0)
    currentExp = models.PositiveIntegerField(default=0)
    nextExp = models.PositiveIntegerField(default=0)
    

class Users(models.Model):
    userid = models.OneToOneField(User)
    username = models.CharField(max_length=30, unique=True)
    location = models.CharField(max_length=30)
    createTime = models.DateTimeField()
    lastLogin = models.DateTimeField()
    lastToken = models.CharField(max_length=32)
    stats = models.OneToOneField(UserStats)