from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_my_slot.models import Availabilities, Reservations, TestModel
from api_my_slot.serializers import AvailabilitieSerializer, ReservationSerializer, TestSerializer
from django.core.files.storage import default_storage

# Availability API
class AvailabilityAPI(APIView):
    def get(self, request):
        availabilities = Availabilities.objects.all()
        serializer = AvailabilitieSerializer(availabilities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvailabilitieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "availability created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            availability = Availabilities.objects.get(id=request.data["id"])
        except Availabilities.DoesNotExist:
            return Response({"error": "availability not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AvailabilitieSerializer(availability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            availability = Availabilities.objects.get(id=id)
            availability.delete()
            return Response({"message": "deleted successfully"}, status=status.HTTP_200_OK)
        except Availabilities.DoesNotExist:
            return Response({"error": "availability not found"}, status=status.HTTP_404_NOT_FOUND)

# Reservation API
class ReservationAPI(APIView):
    def get(self, request):
        reservations = Reservations.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "reservation created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            reservation = Reservations.objects.get(id=request.data["id"])
        except Reservations.DoesNotExist:
            return Response({"error": "reservation not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            reservation = Reservations.objects.get(id=id)
            reservation.delete()
            return Response({"message": "deleted successfully"}, status=status.HTTP_200_OK)
        except Reservations.DoesNotExist:
            return Response({"error": "reservation not found"}, status=status.HTTP_404_NOT_FOUND)

# Test API
class TestAPI(APIView):
    def get(self, request):
        tests = TestModel.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "test created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            test = TestModel.objects.get(id=request.data["id"])
        except TestModel.DoesNotExist:
            return Response({"error": "test not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            test = TestModel.objects.get(id=id)
            test.delete()
            return Response({"message": "deleted successfully"}, status=status.HTTP_200_OK)
        except TestModel.DoesNotExist:
            return Response({"error": "test not found"}, status=status.HTTP_404_NOT_FOUND)