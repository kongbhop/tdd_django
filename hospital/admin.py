from django.contrib import admin
from hospital.models import Patient
from hospital.models import Appointment
# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)

