from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api_my_slot.models import Availabilities, Reservations, TestModel
from api_my_slot.serializers import AvailabilitieSerializer, ReservationSerializer,TestSerializer


from django.core.files.storage import default_storage

# Create your views here.
from django.http import HttpResponse


@csrf_exempt
def availabilitie_api(request, id=0):
    if request.method == 'GET':
        availabilities = Availabilities.objects.all()
        availabilities_serializer = AvailabilitieSerializer(availabilities,many=True)
        return JsonResponse(availabilities_serializer.data, safe=False)
    elif request.method=='POST':
        availabilitie_data = JSONParser().parse(request)
        availabilities_serializer=AvailabilitieSerializer(data=availabilitie_data)
        if availabilities_serializer.is_valid():
            availabilities_serializer.save()
            return JsonResponse("Availabilitie created",safe=False)
        return JsonResponse("Availabilitie was not created", safe=False)
    elif request.method == 'PUT':
        availabilitie_data=JSONParser().parse(request)
        availabilitie=Availabilities.objects.get(id=availabilitie_data['id'])
        availabilities_serializer=AvailabilitieSerializer(availabilitie,data=availabilitie_data)
        if availabilities_serializer.is_valid():
            availabilities_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        availabilitie=Availabilities.objects.get(id=id)
        availabilitie.delete()
        return JsonResponse("Deleted successfully", safe=False)

# crud for reservations
@csrf_exempt
def reservation_api(request, id=0):
    if request.method == 'GET':
        reservations = Reservations.objects.all()
        reservations_serializer = ReservationSerializer(reservations,many=True)
        return JsonResponse(reservations_serializer.data, safe=False)
    elif request.method == 'POST':
        reservation_data = JSONParser().parse(request)
        reservations_serializer = ReservationSerializer(data=reservation_data)

        if reservations_serializer.is_valid():
            reservations_serializer.save()
            return JsonResponse("Reservation created",safe=False)
        return JsonResponse(reservations_serializer.errors , safe=False)
    elif request.method == 'PUT':
        reservation_data=JSONParser().parse(request)
        reservation=Reservations.objects.get(reservationid=reservation_data['id'])
        reservations_serializer=ReservationSerializer(reservation,data=reservation_data)
        if reservations_serializer.is_valid():
            reservations_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        reservation = Reservations.objects.get(id=id)
        reservation.delete()
        return JsonResponse("Deleted successfully", safe=False)

@csrf_exempt
def handl_test_api(request, id=0):
    if request.method == 'GET':
        tests = Tests.objects.all()
        tests_serializer = TestSerializer(tests,many=True)
        return JsonResponse(tests_serializer.data, safe=False)
    elif request.method == 'POST':
        test_data = JSONParser().parse(request)
        # test_data = request
        tests_serializer = TestSerializer(data=test_data)
        if tests_serializer.is_valid():
            tests_serializer.save()
            return JsonResponse("test created",safe=False)
        return JsonResponse("test was not created" , safe=False)
    elif request.method == 'PUT':
        test_data=JSONParser().parse(request)
        test = Tests.objects.get(id=test_data['id'])
        tests_serializer=TestSerializer(test,data=test_data)
        if tests_serializer.is_valid():
            tests_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        reservation = Tests.objects.get(id=id)
        reservation.delete()
        return JsonResponse("Deleted successfully", safe=False)

# storage
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)
