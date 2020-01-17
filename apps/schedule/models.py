from django.utils import timezone

from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.patient.models import Patient
from apps.worker.models import Worker


class Event(models.Model):
    SERVICE_CHOICES = [
        ('ds', _('personal and domestic services')),
        ('cs', _('complementary services')),
        ('ts', _('therapeutic service')),
        ('od', _('other service')),
    ]
    service = models.CharField(_('service'), max_length=200, choices=SERVICE_CHOICES, default='')
    description = models.TextField(_('description'), blank=True)
    worker = models.ForeignKey(
        Worker,
        verbose_name=_('worker'),
        related_name='event',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    patient = models.ForeignKey(
        Patient,
        verbose_name=_('patient'),
        related_name='event',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    date = models.DateField(_('date'), default=timezone.now)
    start_time = models.TimeField(_('hour of the event'),help_text=_('hour of the event'))
    end_time = models.TimeField(_('end hour of the event'), help_text=_('end hour of the event'))
    time = models.DecimalField(max_digits=20, decimal_places=2, blank=True)

    class Meta:
        verbose_name = _('Scheduling')
        verbose_name_plural = _('Scheduling')

    def __str__(self):
        return '{} ({}{} {}-{})'.format(self.worker, self.patient, self.date.strftime("%d:%m"), self.start_time.strftime("%H:%M"), self.end_time.strftime("%H:%M"))
