import datetime
import decimal

from django.db.models import Sum
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.views.decorators import staff_member_required

from apps.schedule.models import Event
from apps.worker.models import Worker
from apps.patient.models import Patient
from apps.schedule.forms import EventForm


def index(request):
    context = {

    }
    return render(request, ('hello'), context)


def create_event(request, dni_worker, dni_patient):

    try:
        worker = Worker.objects.get(dni=dni_worker)
    except :
        worker = ''

    try:
        patient = Patient.objects.get(dni=dni_patient)
    except :
        patient = ''
        print(worker)
        print(patient)
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if patient and worker:
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.worker = worker
                event.patient = patient
                start = datetime.datetime.strptime(str(event.start_time), '%H:%M:%S')
                end = datetime.datetime.strptime(str(event.end_time), '%H:%M:%S')
                event.time = (abs((end-start).seconds)/60)
                event.save()
                messages.success(request, _('event was successfully created')+' {worker}-{patient} ({date} {start}:{end})'.format(
                    worker=event.worker.user.first_name,
                    patient=event.patient.first_name,
                    date=event.date.strftime('%d-%m-%Y'),
                    start=event.start_time.strftime('%H:%M'),
                    end=event.end_time.strftime('%H:%M')
                    )
                )
                reverse('dashboard:create_event', kwargs={'dni_worker': worker.dni, 'dni_patient': patient.dni})
            else:
                messages.error(request, _('Please correct the error below.'))
        else:
            messages.error(request, _('worker or patient no exist'))
    else:
        event_form = EventForm()
    context = {
        'event_form': event_form,
        'patient': patient,
        'worker': worker
    }
    return render(request, 'dashboard/form/event.html', context)


def list_event(request):
    date = timezone.now()
    money = decimal.Decimal(6.50 / 60)
    if request.user.is_staff:
        items = Event.objects.filter(date__month=date.month)
    else:
        items = Event.objects.filter(worker__user__first_name=request.user.first_name, date__month=date.month).order_by('patient', 'date')

    total = items.aggregate(sum=Sum('time'))
    total = total['sum']
    context = {
        'items': items,
        'hour': round(total/60),
        'total': round(total * money)
    }

    return render(request, 'dashboard/view/event_list.html', context)


def print_event(request, year, month, patient):
    money = decimal.Decimal(6.50 / 60)
    worker = ''
    date = ''
    times = ''
    try:
        items = Event.objects.filter(
            date__month=month,
            date__year=year,
            patient__dni=patient
        ).order_by('date')
    except Event.DoesNotExist:
        items = ''

    if items:
        total = items.aggregate(sum=Sum('time')) or 0
        total = total['sum']
        total = total * 60
        hours = total // 3600
        minutes = total // 60 - hours * 60
        times = _("{}hours  {}minutes").format(hours, minutes)
        total = total/60

    else:
        total = 0
    for item in items:
        worker = item.worker
        patient = item.patient
        date = item.date
    context = {
        'items': items,
        'date': date,
        'worker': worker,
        'patient': patient,
        'total_min': total,
        'hour': round(total / 60),
        'total_money': total * money,
        'times':times,

    }

    return render(request, 'dashboard/print/event.html', context)
