from rest_framework import serializers
from ApiMySlot.models import Availabilities,Reservations, Tests


class AvailabilitieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Availabilities 
        fields=('Id','Start', 'End', 'CreatedAt')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservations 
        fields=('Id','Title','Email','Start','End', 'CreatedAt')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tests 
        fields=('Id','Title')
