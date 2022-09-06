from django.db import models

class Availabilities(models.Model):
    Id = models.AutoField(primary_key=True)
    Start = models.CharField(max_length=500)
    End = models.CharField(max_length=500)
    CreatedAt = models.DateField()

class Reservations(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
    Start = models.DateField()
    End = models.DateField()
    CreatedAt = models.DateField()


