from django.test import TestCase
from ..models import (
	Patient,
	Appointment
)


class PatientViewTest(TestCase):
    def setUp(self):
        patient = Patient()
        patient.med_id = 'med4611'
        patient.age = 50
        patient.height = 160
        patient.weight = 45
        patient.save()

        self.url = '/viewPatient/'

    def test_agent_should_see_correct_patient_data(self):
        response = self.client.get(self.url)
        pass
