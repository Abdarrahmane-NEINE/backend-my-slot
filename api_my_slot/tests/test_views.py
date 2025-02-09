import pytest
import json
from django.utils.timezone import now
from rest_framework.test import APIClient
from api_my_slot.models import Availabilities, Reservations, TestModel

@pytest.mark.django_db
def test_create_availability():
    """Test creating an availability using POST API"""
    client = APIClient()
    payload = {"start": "2025-02-01T10:00:00Z", "end": "2025-02-01T11:00:00Z"}
    
    response = client.post("/availabilities", payload, format="json")
    
    assert response.status_code == 201  # HTTP 201 Created
    assert response.data["message"] == "availability created"
    assert Availabilities.objects.count() == 1  # Ensure it's saved in DB

@pytest.mark.django_db
def test_get_availabilities():
    """Test retrieving all availabilities"""
    client = APIClient()
    
    # Create some availabilities
    Availabilities.objects.create(start=now(), end=now())
    Availabilities.objects.create(start=now(), end=now())

    response = client.get("/availabilities")

    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 2  # Should return 2 availabilities

@pytest.mark.django_db
def test_update_availability():
    """Test updating an existing availability"""
    client = APIClient()
    
    availability = Availabilities.objects.create(start=now(), end=now())

    payload = {"id": availability.id, "start": "2025-02-01T10:00:00Z", "end": "2025-02-01T11:00:00Z"}
    response = client.put("/availabilities", payload, format="json")

    assert response.status_code == 200
    availability.refresh_from_db()
    assert str(availability.start) == "2025-02-01 10:00:00+00:00"
    assert str(availability.end) == "2025-02-01 11:00:00+00:00"

@pytest.mark.django_db
def test_delete_availability():
    """Test deleting an availability"""
    client = APIClient()
    
    availability = Availabilities.objects.create(start=now(), end=now())

    response = client.delete(f"/availabilities/{availability.id}")

    assert response.status_code == 200
    assert response.data["message"] == "deleted successfully"
    assert Availabilities.objects.count() == 0

@pytest.mark.django_db
def test_create_availability_invalid():
    """Test creating an availability with missing fields"""
    client = APIClient()
    payload = {}  # Missing 'start' and 'end'
    
    response = client.post("/availabilities", payload, format="json")
    
    assert response.status_code == 400
    assert "start" in response.data  # Should return validation errors
    assert "end" in response.data

@pytest.mark.django_db
def test_update_availability_not_found():
    """Test updating an availability that does not exist"""
    client = APIClient()
    payload = {"id": 9999, "start": "2025-02-01T10:00:00Z", "end": "2025-02-01T11:00:00Z"}
    
    response = client.put("/availabilities", payload, format="json")
    
    assert response.status_code == 404
    assert response.data["error"] == "availability not found"

@pytest.mark.django_db
def test_update_availability_invalid():
    """Test updating an availability with invalid data"""
    client = APIClient()
    
    # Create an availability entry
    availability = Availabilities.objects.create(start=now(), end=now())

    # Send an update request with missing required fields
    payload = {"id": availability.id, "start": ""}  # Missing 'end' field
    response = client.put("/availabilities", payload, format="json")

    assert response.status_code == 400
    assert "start" in response.data or "end" in response.data  # Validation should fail

@pytest.mark.django_db
def test_delete_availability_not_found():
    """Test deleting an availability that does not exist"""
    client = APIClient()
    response = client.delete("/availabilities/9999")
    
    assert response.status_code == 404
    assert response.data["error"] == "availability not found"

@pytest.mark.django_db
def test_create_reservation():
    """Test creating a reservation"""
    client = APIClient()
    payload = {"title": "Test Meeting", "email": "test@example.com", "start": "2024-01-01T10:00:00Z", "end": "2024-01-01T11:00:00Z"}

    response = client.post("/reservations", payload, format="json")

    assert response.status_code == 201  # HTTP 201 Created
    assert response.data["message"] == "reservation created"
    assert Reservations.objects.count() == 1

@pytest.mark.django_db
def test_get_reservations():
    """Test retrieving all reservations"""
    client = APIClient()

    # Create sample reservations
    Reservations.objects.create(title="Meeting 1", email="user1@example.com", start=now(), end=now())
    Reservations.objects.create(title="Meeting 2", email="user2@example.com", start=now(), end=now())

    response = client.get("/reservations")

    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 2

@pytest.mark.django_db
def test_update_reservation():
    """Test updating an existing reservation"""
    client = APIClient()
    
    reservation = Reservations.objects.create(title="Meeting", email="user@example.com", start=now(), end=now())

    payload = {
        "id": reservation.id, 
        "title": "Updated Meeting", 
        "email": "new@example.com",
        "start": now(), 
        "end": now()
    }
    response = client.put("/reservations", payload, format="json")

    assert response.status_code == 200
    reservation.refresh_from_db()
    assert reservation.title == "Updated Meeting"
    assert reservation.email == "new@example.com"

@pytest.mark.django_db
def test_delete_reservation():
    """Test deleting a reservation"""
    client = APIClient()
    
    reservation = Reservations.objects.create(title="To Delete", email="user@example.com", start=now(), end=now())

    response = client.delete(f"/reservations/{reservation.id}")

    assert response.status_code == 200
    assert response.data["message"] == "deleted successfully"
    assert Reservations.objects.count() == 0

@pytest.mark.django_db
def test_create_reservation_invalid():
    """Test creating a reservation with missing fields"""
    client = APIClient()
    payload = {"title": "No email"}  # Missing 'email', 'start', 'end'

    response = client.post("/reservations", payload, format="json")
    
    assert response.status_code == 400
    assert "email" in response.data
    assert "start" in response.data
    assert "end" in response.data

@pytest.mark.django_db
def test_update_reservation_not_found():
    """Test updating a reservation that does not exist"""
    client = APIClient()
    payload = {"id": 9999, "title": "Updated Meeting", "email": "new@example.com"}

    response = client.put("/reservations", payload, format="json")
    
    assert response.status_code == 404
    assert response.data["error"] == "reservation not found"

@pytest.mark.django_db
def test_update_reservation_invalid():
    """Test updating a reservation with invalid data"""
    client = APIClient()
    
    reservation = Reservations.objects.create(
        title="Meeting", email="user@example.com", start=now(), end=now()
    )

    payload = {"id": reservation.id, "title": ""}  # Empty title (invalid)
    response = client.put("/reservations", payload, format="json")

    assert response.status_code == 400  # Should fail
    assert "title" in response.data  # Should return validation error

@pytest.mark.django_db
def test_delete_reservation_not_found():
    """Test deleting a reservation that does not exist"""
    client = APIClient()
    response = client.delete("/reservations/9999")

    assert response.status_code == 404
    assert response.data["error"] == "reservation not found"

@pytest.mark.django_db
def test_create_test():
    """Test creating a test entry using POST API"""
    client = APIClient()
    payload = {"title": "Unit Test"}

    response = client.post("/tests", payload, format="json")

    assert response.status_code == 201  # HTTP 201 Created
    assert response.data["message"] == "test created"
    assert TestModel.objects.count() == 1

@pytest.mark.django_db
def test_get_tests():
    """Test retrieving all test entries"""
    client = APIClient()
    
    # Create sample test entries
    TestModel.objects.create(title="Test 1")
    TestModel.objects.create(title="Test 2")

    response = client.get("/tests")

    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 2

@pytest.mark.django_db
def test_update_test():
    """Test updating an existing test entry"""
    client = APIClient()
    test_entry = TestModel.objects.create(title="Old Title")

    payload = {"id": test_entry.id, "title": "Updated Title"}
    response = client.put("/tests", payload, format="json")

    assert response.status_code == 200
    test_entry.refresh_from_db()
    assert test_entry.title == "Updated Title"

@pytest.mark.django_db
def test_delete_test():
    """Test deleting a test entry"""
    client = APIClient()
    test_entry = TestModel.objects.create(title="To Be Deleted")

    response = client.delete(f"/tests/{test_entry.id}")

    assert response.status_code == 200
    assert response.data["message"] == "deleted successfully"
    assert TestModel.objects.count() == 0

@pytest.mark.django_db
def test_create_test_empty_payload():
    """Test creating a test entry with an empty payload"""
    client = APIClient()
    payload = {}  # No data

    response = client.post("/tests", payload, format="json")

    assert response.status_code == 400  # Should fail
    assert "title" in response.data  # Should return validation error

@pytest.mark.django_db
def test_delete_test_not_found():
    """Test deleting a test entry that does not exist"""
    client = APIClient()
    response = client.delete("/tests/9999")

    assert response.status_code == 404
    assert response.data["error"] == "test not found"

@pytest.mark.django_db
def test_update_test_not_found():
    """Test updating a test that does not exist"""
    client = APIClient()
    
    payload = {"id": 9999, "title": "Updated Title"}
    response = client.put("/tests", payload, format="json")

    assert response.status_code == 404
    assert response.data["error"] == "test not found"

@pytest.mark.django_db
def test_update_test_invalid():
    """Test updating a test with invalid data"""
    client = APIClient()
    
    test_entry = TestModel.objects.create(title="Valid Title")

    payload = {"id": test_entry.id, "title": ""}  # Invalid empty title
    response = client.put("/tests", payload, format="json")

    assert response.status_code == 400
    assert "title" in response.data  # Should return a validation error
