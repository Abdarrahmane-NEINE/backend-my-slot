from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ApiMySlot.models import Availabilities, Reservations
from ApiMySlot.serializers import AvailabilitieSerializer, ReservationSerializer

from django.core.files.storage import default_storage

# Create your views here.
from django.http import HttpResponse

from ApiMySlot.models import Availabilities

# def index(request):
#     return HttpResponse("Hello, world. You're at the ApiMySlot index.")

@csrf_exempt
def availabilitieApi(request, id=0):
    if request.method == 'GET':
        availabilities = Availabilities.objects.all()
        availabilities_serializer = AvailabilitieSerializer(availabilities,many=True)
        return JsonResponse(availabilities_serializer.data, sage=False)
    elif request.method=='POST':
        availabilitie_data = JSONParser().parse(request)
        availabilities_serializer = AvailabilitieSerializer(data=availabilitie_data)
        if availabilities_serializer.is_valid():
            availabilities_serializer.save()
            return JsonResponse("Availabilitie created",safe=False)
        return JsonResponse("Availabilitie was not created", safe=False)
    elif request.method == 'PUT':
        availabilitie_data=JSONParser().parse(request)
        availabilitie=Availabilities.objects.get(availabilitieId=availabilitie_data['availabilitieId'])
        availabilities_serializer=AvailabilitieSerializer(availabilitie,data=availabilitie_data)
        if availabilities_serializer.is_valid():
            availabilities_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        availabilitie=Availabilities.objects.get(availabilitieId=id)
        availabilitie.delete()
        return JsonResponse("Deleted successfully", safe=False)

# crud for reservations
@csrf_exempt
def reservationApi(request, id=0):
    if request.method == 'GET':
        reservations = Reservations.objects.all()
        reservations_serializer = ReservationSerializer(reservations,many=True)
        return JsonResponse(reservations_serializer.data, sage=False)
    elif request.method == 'POST':
        reservation_data = JSONParser().parse(request)
        reservations_serializer = ReservationSerializer(data=reservation_data)
        if reservations_serializer.is_valid():
            reservations_serializer.save()
            return JsonResponse("Reservation created",safe=False)
        return JsonResponse("Reservation was not created", safe=False)
    elif request.method == 'PUT':
        reservation_data=JSONParser().parse(request)
        reservation = Reservations.objects.get(reservationId=reservation_data['reservationId'])
        reservations_serializer=ReservationSerializer(reservation,data=reservation_data)
        if reservations_serializer.is_valid():
            reservations_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        reservation = Reservations.objects.get(reservationId=id)
        reservation.delete()
        return JsonResponse("Deleted successfully", safe=False)

# storage
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)
