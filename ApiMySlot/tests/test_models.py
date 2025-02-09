import pytest
from ApiMySlot.models import Availabilities, Reservations
from django.utils.timezone import now

@pytest.mark.django_db
def test_create_availability():
    availability = Availabilities.objects.create(
        Start=now(), End=now()
    )
    assert availability.Id is not None

@pytest.mark.django_db
def test_create_reservation():
    reservation = Reservations.objects.create(
        Title="Meeting",
        Email="user@example.com",
        Start=now(),
        End=now()
    )
    assert reservation.Id is not None
    assert reservation.Title == "Meeting"
    assert reservation.Email == "user@example.com"
