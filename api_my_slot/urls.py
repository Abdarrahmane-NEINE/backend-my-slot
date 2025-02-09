from django.urls import path
from api_my_slot.views import AvailabilityAPI, ReservationAPI, TestAPI

urlpatterns = [
    path("availabilities", AvailabilityAPI.as_view(), name="availabilities"),
    path("availabilities/<int:id>", AvailabilityAPI.as_view(), name="availabilities_detail"),

    path("reservations", ReservationAPI.as_view(), name="reservations"),
    path("reservations/<int:id>", ReservationAPI.as_view(), name="reservations_detail"),

    path("tests", TestAPI.as_view(), name="tests"),
    path("tests/<int:id>", TestAPI.as_view(), name="tests_detail"),
]
