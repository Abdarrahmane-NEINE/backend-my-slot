from django.db import models
import datetime

class Availabilities(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.DateTimeField("%Y-%m-%d %h:%m")
    start.editable= True
    end = models.DateTimeField("%Y-%m-%d  %h:%m")
    end.editable= True
    created_at = models.DateTimeField(auto_now=True)

class Reservations(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    start = models.DateTimeField("%Y-%m-%d %h:%m")
    start.editable= True
    end = models.DateTimeField("%Y-%m-%d %h:%m")
    end.editable= True
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class TestModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)