import pytest
from django.http import JsonResponse
from django.utils.timezone import now
from rest_framework.parsers import JSONParser
from api_my_slot.models import Availabilities, Reservations, TestModel
from api_my_slot.views import availabilitie_api, reservation_api, handl_test_api
from django.test import RequestFactory

@pytest.mark.django_db
def test_get_availabilities():
    factory = RequestFactory()
    request = factory.get("/availabilitie")
    response = availabilitie_api(request)
    
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_reservation():
    factory = RequestFactory()
    request = factory.post("/reservation", content_type="application/json", data='{"title": "Test Meeting", "email": "test@example.com", "start": "2024-01-01T10:00:00Z", "end": "2024-01-01T11:00:00Z"}')

    response = reservation_api(request)
    assert response.status_code == 200
    assert "created" in response.content.decode()
