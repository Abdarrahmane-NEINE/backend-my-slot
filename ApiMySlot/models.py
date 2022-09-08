from django.db import models
import datetime

class Availabilities(models.Model):
    Id = models.AutoField(primary_key=True)
    # Start = models.DateTimeField("%mm.%d.%YYYY %h:%mm aa")
    # Start = models.DateTimeField("%Y-%m-%d %I")
    Start = models.DateTimeField("%Y-%m-%d %h:%m")
    # Start = models.DateTimeField(default=timezone.now)
    Start.editable= True
    # End = models.DateTimeField("%mm.%d.%YYYY %h:%mm aa")
    End = models.DateTimeField("%Y-%m-%d  %h:%m")
    End.editable= True
    CreatedAt = models.DateTimeField(auto_now=True)

class Reservations(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)
    Email = models.EmailField(max_length=254)
    Start = models.DateTimeField(auto_now=False)
    Start.editable= True
    End = models.DateTimeField(auto_now=False)
    End.editable= True
    CreatedAt = models.DateTimeField(auto_now=True)

class Tests(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)