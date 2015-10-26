from django.test import TestCase
from ..models import (
	Patient,
	Appointment
)

# Create your tests here.
class PatientTest(TestCase):
	def test_can_save_patient(self):
		patient = Patient()
		self.assertFalse(patient.id)

		patient.med_id = 'med2321'
		patient.age = 22
		patient.weight = 65
		patient.height = 170
		patient.save()
		self.assertTrue(patient.id)

		selected_patient = Patient.objects.all()
		self.assertEqual(1, len(selected_patient))
		self.assertEqual('med2321', selected_patient[0].med_id)
		self.assertEqual(22, selected_patient[0].age)
		self.assertEqual(65, selected_patient[0].weight)
		self.assertEqual(170, selected_patient[0].height)