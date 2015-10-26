from django.db import models


class Patient(models.Model):
    med_id = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()


class Appointment(models.Model):
    patient = models.ForeignKey(Patient)
    doctor_id = models.IntegerField()
    date = models.DateTimeField()
