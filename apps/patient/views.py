
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.views.decorators import staff_member_required

from apps.patient.models import Patient
from apps.patient.forms import PatientForm


@staff_member_required
def create_patient(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST, request.FILES)
        if patient_form.is_valid():
            patient = patient_form.save(commit=False)
            patient.active_status = True
            try:
                item = Patient.objects.filter(
                    dni=patient.dni,
                    first_name=patient.first_name
                )
            except Patient.DoesNotExist:
                item = None

            if not item:
                patient.save()
                messages.success(request, _('patient was successfully created'))
                return redirect('dashboard:home')
            else:
                item = False
                messages.error(request, _('the patient already exist'))
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        patient_form = PatientForm()
    context = {
        'patient_form': patient_form,
    }
    return render(request, 'dashboard/form/patient.html', context)


@staff_member_required
def list_patient(request):

    items = Patient.actives.all()

    context = {
        'items': items,
    }

    return render(request, 'dashboard/view/patient_list.html', context)
