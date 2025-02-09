import pytest
from api_my_slot.models import Availabilities, Reservations
from django.utils.timezone import now

@pytest.mark.django_db
def test_create_availability():
    availability = Availabilities.objects.create(
        start=now(), end=now()
    )
    assert availability.id is not None

@pytest.mark.django_db
def test_create_reservation():
    reservation = Reservations.objects.create(
        title="Meeting",
        email="user@example.com",
        start=now(),
        end=now()
    )
    assert reservation.id is not None
    assert reservation.title == "Meeting"
    assert reservation.email == "user@example.com"
