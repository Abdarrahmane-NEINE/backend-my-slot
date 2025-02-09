import pytest
from api_my_slot.serializers import AvailabilitieSerializer, ReservationSerializer
from api_my_slot.models import Availabilities, Reservations
from django.utils.timezone import now

@pytest.mark.django_db
def test_availability_serializer():
    data = {"start": now(), "end": now()}
    serializer = AvailabilitieSerializer(data=data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_invalid_reservation_serializer():
    data = {"title": "", "email": "not-an-email"}  # Invalid title and email
    serializer = ReservationSerializer(data=data)
    assert not serializer.is_valid()
    assert "title" in serializer.errors
    assert "email" in serializer.errors
