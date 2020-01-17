import datetime
import decimal

from django.db.models import Sum
from django.utils import timezone
from django import template

from apps.frontend.models import Link
from apps.schedule.models import Event
from apps.blog.models import BlogPost
from apps.worker.models import Worker
from apps.patient.models import Patient

timezone_today = timezone.localtime(timezone.now()).date()

register = template.Library()

# @register.simple_tag()
# def call(instance, function, *args, **kwargs):
#     func = instance.__meta__.get_function(function)
#     return func(*args, **kwargs)


# @register.simple_tag()
# def list(instance, month, location_pk, category_pk):
#     return instance.show()

@register.inclusion_tag('inc/children.html')
def children(item, hook=None, lang=None):
    try:
        items = Link.objects.filter(pk=item.pk).get_descendants(include_self=False)
    except Link.DoesNotExist:
        items = ''
    context = {
        'item': items,
        'hook': hook,
        'lang': lang
    }

    return context


@register.simple_tag()
def show(instance, title=True):
    return instance.show(title=title)


@register.inclusion_tag('inc/mapleaflet.html')
def map(item, latitude=None, longitude=None):
    item.latitude = latitude if latitude else item.latitude
    item.longitude = longitude if longitude else item.longitude

    context = {
        'item': item
    }

    return context


@register.inclusion_tag('inc/table_patient.html')
def show_table(worker=None, patient=None):
    date = timezone.now()
    money = decimal.Decimal(6.50 / 60)
    id_name = patient.first_name.replace(' ','')
    items = Event.objects.filter(worker__user__first_name=worker.first_name, date__month=date.month, patient__dni=patient.dni).order_by('date')
    if items:
        total = items.aggregate(sum=Sum('time')) or 0
        total = total['sum']
    else:
        total = 0

    context = {
        'name_worker': worker.worker.full_name,
        'patient': patient,
        'id_name': id_name,
        'month': date.month,
        'year': date.year,
        'items': items,
        'total_min': total,
        'hour': round(total / 60),
        'total_money': total * money,
    }
    return context


@register.inclusion_tag('inc/activities.html')
def activities(items):
    try:
        items = items.filter(date=timezone).order_by('start_time')
    except:
        items = ''

    context = {
        'items': items,
    }

    return context


@register.inclusion_tag('inc/worker_info.html')
def worker_info(items):
    gain_for_day = ''
    gain_for_month = ''
    money = decimal.Decimal(6.50 / 60)
    items = items
    try:
        number_events = items.filter(date=timezone_today).count()
    except:
        number_events = ""
    try:
        min_for_day = items.filter(date=timezone_today)
    except:
        min_for_day = ''
    try:
        events_to_date = items.filter(date__range=(timezone_today.replace(day=1), timezone_today))
    except:
        events_to_date = 0

    if min_for_day:
        min_for_day = min_for_day.aggregate(sum=Sum('time')) or 0
        min_for_day = min_for_day['sum']
        gain_for_day = round(min_for_day * money)

    if events_to_date:
        events_to_date = events_to_date.aggregate(sum=Sum('time')) or 0
        events_to_date = events_to_date['sum']
        gain_for_month = round(events_to_date * money)

    context = {
        'items': items,
        'events_to_date': events_to_date,
        'number_events': number_events,
        'min_for_day': min_for_day,
        'gain_for_day': gain_for_day,
        'gain_for_month': gain_for_month,
    }

    return context


@register.inclusion_tag('inc/featured_posts.html')
def featured_posts():
    try:
        items = BlogPost.actives.all().order_by('date_active_ini')[0:3]
    except:
        items = ''

    context = {
        'items': items,
    }

    return context


@register.inclusion_tag('inc/admin_info.html')
def admin_info():
    try:
        num_workers = Worker.actives.all().count()
    except:
        num_workers = 0

    try:
        num_patients = Patient.actives.all().count()
    except:
        num_patients = 0

    try:
        events_today = Event.objects.filter(date=timezone_today).count()
    except:
        events_today = 0

    try:
        events_month = Event.objects.filter(date__month=timezone_today.month()).count()
    except:
        events_month = 0

    context = {
        'num_workers': num_workers,
        'num_patients': num_patients,
        'events_today': events_today,
        'events_month': events_month,
    }

    return context
