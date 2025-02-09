from rest_framework import serializers
from api_my_slot.models import Availabilities,Reservations, TestModel


class AvailabilitieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Availabilities 
        fields=('id','start', 'end', 'created_at')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservations 
        fields=('id','title','email','start','end', 'created_at')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=TestModel 
        fields=('id','title')
