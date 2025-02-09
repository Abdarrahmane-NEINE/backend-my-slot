import pytest
from ApiMySlot.serializers import AvailabilitieSerializer, ReservationSerializer
from ApiMySlot.models import Availabilities, Reservations
from django.utils.timezone import now

@pytest.mark.django_db
def test_availability_serializer():
    data = {"Start": now(), "End": now()}
    serializer = AvailabilitieSerializer(data=data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_invalid_reservation_serializer():
    data = {"Title": "", "Email": "not-an-email"}  # Invalid title and email
    serializer = ReservationSerializer(data=data)
    assert not serializer.is_valid()
    assert "Title" in serializer.errors
    assert "Email" in serializer.errors
