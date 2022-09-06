from rest_framework import serializers
from ApiMySlot.models import Availabilities,Reservations

class AvailabilitieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Availabilities 
        fields=('Id','Start', 'End', 'CreatedAt')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservations 
        fields=('Id','Title','Email','Start','End', 'CreatedAt')