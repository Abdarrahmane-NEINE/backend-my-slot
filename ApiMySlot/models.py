from django.db import models

class Availabilities(models.Model):
    availabilitieId = models.AutoField(primary_key=True)
    availabilitieStart = models.CharField(max_length=500)
    availabilitieEnd = models.CharField(max_length=500)
    availabilitieCreatedAt = models.DateField()

class Reservations(models.Model):
    resevationId = models.AutoField(primary_key=True)
    reservationTitle = models.CharField(max_length=500)
    reservationEmail = models.CharField(max_length=500)
    reservationStart = models.DateField()
    reservationEnd = models.DateField()
    reservationCreatedAt = models.DateField()


