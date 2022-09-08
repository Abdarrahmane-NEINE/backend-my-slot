from django.db import models
import datetime

class Availabilities(models.Model):
    Id = models.AutoField(primary_key=True)
    Start = models.DateTimeField("%Y-%m-%d %h:%m")
    Start.editable= True
    End = models.DateTimeField("%Y-%m-%d  %h:%m")
    End.editable= True
    CreatedAt = models.DateTimeField(auto_now=True)

class Reservations(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)
    Email = models.EmailField(max_length=254)
    Start = models.DateTimeField("%Y-%m-%d %h:%m")
    Start.editable= True
    End = models.DateTimeField("%Y-%m-%d %h:%m")
    End.editable= True
    CreatedAt = models.DateTimeField("%Y-%m-%d %h:%m")

class Tests(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)