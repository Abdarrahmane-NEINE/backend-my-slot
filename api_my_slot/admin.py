from django.contrib import admin
from .models import Availabilities, Reservations, TestModel
# models
admin.site.register(Availabilities)
admin.site.register(Reservations)
admin.site.register(TestModel)