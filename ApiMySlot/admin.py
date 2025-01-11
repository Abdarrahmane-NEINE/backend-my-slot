from django.contrib import admin
from .models import Availabilities, Reservations, Tests
# models
admin.site.register(Availabilities)
admin.site.register(Reservations)
admin.site.register(Tests)