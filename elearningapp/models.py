from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib import admin
import os


# Create your models here.
class Userregistrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    Password = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_photo = models.FileField()

    def str(self):
        return self.username

class course_registration(models.Model):
    # register_id=models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=200)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    qualification = models.CharField(max_length=250)


class registration1(models.Model):
    name = models.CharField(max_length=200)
    gmail = models.EmailField(max_length=25)
    phoneno = models.IntegerField()
    course = models.CharField(max_length=25)
    Qualification = models.CharField(max_length=25)


    # user_image =models.ImageField(upload_to='course/')
    def str(self):
        return self.name
class course_data(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_name=models.CharField(max_length=250)

class payment(models.Model):
    name=models.CharField(max_length=250)
    gmail=models.EmailField(max_length=250)
    phoneno = models.IntegerField()
    course=models.CharField(max_length=250)
    amount=models.CharField(max_length=250)
    payment_id=models.CharField(max_length=250)
    status_choice = [
        ('Lock', 'Lock'),
        ('reject', 'reject'),
        ('Unlock', 'Unlock'),
    ]
    status = models.CharField(max_length=10, choices=status_choice)

    def str(self):
        return self.name
class trainer_reg(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    phoneno = models.IntegerField()
    trainerphoto = models.FileField()
    password=models.CharField(max_length=25)
    status_choice = [
        ('approve', 'approve'),
        ('reject', 'reject'),
        ('pending', 'pending'),
    ]
    status = models.CharField(max_length=10, choices=status_choice, default='pending')
    def str(self):
        return self.name


class certificates(models.Model):
    name = models.CharField(max_length=250)
    sslc=models.FileField()
    plus_two=models.FileField()
    degree=models.FileField()

#class Student(models.Model):
#    name = models.OneToOneField(payment, on_delete=models.CASCADE)
#    is_blocked = models.BooleanField(default=False)


class placementreg(models.Model):
    name = models.CharField(max_length=200)
    gmail = models.EmailField(max_length=25)
    phoneno = models.IntegerField()
    cv=models.FileField(upload_to='media')
    position = models.CharField(max_length=25)
    Qualification = models.CharField(max_length=25)

    # user_image =models.ImageField(upload_to='course/')
    def str(self):
        return self.name
class interview_reg(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    phoneno=models.IntegerField()
    course = models.CharField(max_length=250)
    Qualification = models.CharField(max_length=250)
    def str(self):
        return self.name
