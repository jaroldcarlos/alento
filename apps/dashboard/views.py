from django.utils import timezone


from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from apps.schedule.models import Event


def home(request):
    worker_events = ''
    if request.user.is_staff:
        context = {

        }
        return render(request, 'dashboard/dashboard_admin.html', context)

    try:
        worker_events = Event.objects.filter(worker__user__username=request.user.username)
    except Event.DoesNotExist:
        worker_events = ''

    context = {
        'worker_events': worker_events,
    }

    return render(request, 'dashboard/dashboard_worker.html', context)


def calendar(request):
    try:
        items = Event.objects.all()
    except Event.DoesNotExist:
        items = ''

    context = {
        'items': items,
        'month': _('month')
    }

    return render(request, 'dashboard/view/calendar_list.html', context)
