# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    isApproved = models.CharField(max_length=10,default="no")

    def __str__(self):
        return self.user.username
    def as_json(self):
        return dict(type=self.type,isApproved=self.isApproved,username=self.user.username)

class AdminDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=10)
    rollno = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=10)
    year = models.IntegerField()
    contact = models.BigIntegerField()
    profilepicture = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.name



