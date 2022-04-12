# todo/models.py
from django.db import models
from django.db import migrations
from django import forms




class User(models.Model):   
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    #password = models.CharField(max_length=20, widget=forms.PasswordInput)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

class Release(models.Model):
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    press_release = models.TextField(null=True)
    release_date = models.DateField()