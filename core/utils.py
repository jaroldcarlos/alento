import hashlib
import locale
import logging
import random
import string

from calendar import HTMLCalendar
from datetime import datetime, timezone, timedelta

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views.static import serve

from apps.schedule.models import Event

locale.setlocale(locale.LC_ALL, )


@login_required
def protected_serve1(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    logger = logging.getLogger(__name__)

    folder = (path.split('/')[0])
    if folder == "invoices":
        if request.user.is_authenticated:
            if request.user.is_staff:
                return serve(request, path, document_root, show_indexes)
            from apps.voucher.models import Voucher
            reference = (path.split('/')[1].split('_')[1])
            voucher = get_object_or_404(Voucher, reference=reference)

            if voucher.partner().id == request.user.partner.id:
                return serve(request, path, document_root, show_indexes)

        return HttpResponseNotFound("restricted access")

    return serve(request, path, document_root, show_indexes)


def is_in_group(user, group):
    return user.groups.filter(name=group).exists()


def user_is_admin(user):
    return is_in_group(user,'admin')


def user_is_staff(user):
    return is_in_group(user,'staff')


def user_is_user(user):
    return is_in_group(user,'user')


def not_in_agents_group(user):
    return user.groups.filter(name='Agents').count() == 0 if user else False


def create_random_string(length=30):
    if length <= 0:
        length = 30

    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(symbols) for _ in range(length)])


def humanreadable_timedelta(
        theDateAndTime,
        precise=False,
        complete=False,
        fromDate=None):

    if not theDateAndTime:
        return ""
    if not fromDate:
        fromDate = datetime.now(timezone.utc)
    if theDateAndTime > fromDate:
        return None
    elif theDateAndTime == fromDate:
        return _('now')

    delta = fromDate - theDateAndTime

    '''
    the timedelta structure does not have all units; bigger units are converted
    into smaller ones (hours -> seconds, minutes -> seconds, weeks > days, ...)
    but we need all units:
    '''
    deltaMinutes = delta.seconds // 60
    deltaHours = delta.seconds // 3600
    deltaYears = delta.days // 365
    deltaMonths = delta.days // 30
    deltaMinutes -= deltaHours * 60
    deltaWeeks = delta.days // 7
    deltaSeconds = delta.seconds - deltaMinutes * 60 - deltaHours * 3600
    deltaDays = delta.days - deltaWeeks * 7
    deltaMilliSeconds = delta.microseconds // 1000
    deltaMicroSeconds = delta.microseconds - deltaMilliSeconds * 1000

    valuesAndNames = [
        (deltaYears, _('year')),
        (deltaMonths, _('month')),
        (deltaWeeks, _('week')),
        (deltaDays, _('day')),
        (deltaHours, _('hour')),
        (deltaMinutes, _('minute')),
        (deltaSeconds, _('second'))
    ]
    if precise:
        valuesAndNames.append((deltaMilliSeconds, _('millisecond')))
        valuesAndNames.append((deltaMicroSeconds, _('microsecond')))

    text = ""
    for value, name in valuesAndNames:
        if value > 0:
            if complete:
                text += len(text) and ", " or ""
                text += "%d %s" % (value, name)
                text += (value > 1) and "s" or ""
            else:
                text += "%d %s" % (value, name)
                text += (value > 1) and "s" or ""
                break

    # replacing last occurrence of a comma by an 'and'
    if text.find(",") > 0:
        text = " and ".join(text.rsplit(", ", 1))

    return text


def calc_year(year):
    if year is None:
        return datetime.now().year
    elif year < 1000:
        return datetime.now().year + year


def calc_month():
    return datetime.now().month


def currency(value):
    if not value:
        value = 0
    return locale.currency(value, symbol=True, grouping=True)


def save_signature(datauri, invoice):
    import os
    from binascii import a2b_base64
    from django.conf import settings
    binary_data = a2b_base64(datauri)
    path=os.path.join(settings.MEDIA_ROOT, 'signatures', '{0:05d}.jpg'.format(invoice.pk))
    with open(path, 'wb') as fd:
        fd.write(binary_data)
