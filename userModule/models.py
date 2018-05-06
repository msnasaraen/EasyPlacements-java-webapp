# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



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

    def as_jsonValue(self):
        return dict(name=self.name,dept=self.dept,rollno=self.rollno,gender=self.gender,birthday=self.birthday,year=self.year,contact=self.contact,profilepicture=self.profilepicture.url)

    def as_filteredAdmin(self):
        return dict(name=self.name,rollno=self.rollno,branch=self.dept,year=self.year,url=self.profilepicture.url,email=self.user.email,id=Role.objects.get(user=self.user).id)



class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=10)
    rollno = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=10)
    year = models.IntegerField()
    contact = models.BigIntegerField()
    cgpa = models.FloatField()
    profilepicture = models.FileField(blank=True,null=True)
    resume = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.name

    def as_jsonUser(self):
        return dict(name=self.name,dept=self.dept,rollno=self.rollno,address=self.address,gender=self.gender,birthday=self.birthday,year=self.year,contact=self.contact,cgpa=self.cgpa,profilepicture=self.profilepicture.url,resume=self.resume.url)

    def as_filteredUser(self):
        return dict(name=self.name,rollno=self.rollno,branch=self.dept,year=self.year,url=self.profilepicture.url,email=self.user.email,id=Role.objects.get(user=self.user).id)



class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    isApproved = models.CharField(max_length=10,default="no")
    isDetailsProvided = models.CharField(max_length=10,default="no")

    def __str__(self):
        return self.user.username

    def as_json(self):
        return dict(type=self.type,isDetailsProvided=self.isDetailsProvided,isApproved=self.isApproved,username=self.user.username)

    def as_jsonApproveUser(self):
        email = User.objects.get(username=self.user).email
        print email
        userDetails = UserDetails.objects.get(user=self.user)
        return dict(name=userDetails.name,rollno=userDetails.rollno,branch=userDetails.dept,year=userDetails.year,url=userDetails.profilepicture.url,email=email,id=Role.objects.get(user=userDetails.user).id)

    def as_getEmail(self):
        return self.user.id


    def as_jsonApproveAdmin(self):
        email = User.objects.get(username=self.user).email
        print email
        userDetails = AdminDetails.objects.get(user=self.user)
        return dict(name=userDetails.name,rollno=userDetails.rollno,branch=userDetails.dept,year=userDetails.year,url=userDetails.profilepicture.url,email=email,id=Role.objects.get(user=userDetails.user).id)


