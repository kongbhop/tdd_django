from django.shortcuts import render
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
)
from .models import Patient


def view_patient_data(request):
	template_name = '../templates/data.html'

	return render(
		request,
		template_name,
		{} #data
	)