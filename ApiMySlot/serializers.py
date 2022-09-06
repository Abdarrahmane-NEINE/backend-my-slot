from rest_framework import serializers
from ApiMySlot.models import Availabilities,Reservations

class AvailabilitieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Availabilities 
        fields=('availabilitieId','availabilitieStart', 'availabilitieEnd', 'availabilitieCreatedAt')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservations 
        fields=('resevationId','reservationTitle','reservationEmail','reservationStart','reservationEnd', 'reservationCreatedAt')