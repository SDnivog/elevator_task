from django.contrib import admin
from .models import Elevator, ElevatorSystem

# Register the models with the admin site
admin.site.register(Elevator)
admin.site.register(ElevatorSystem)