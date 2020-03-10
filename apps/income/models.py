
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.abstract import PaymentModel


def validate_report_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(_('Only PDF files allowed'))


class Income(PaymentModel):

    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        related_name='incomes',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    invoice_file = models.FileField(
        _('invoice file'),
        upload_to='incomes/',
        validators=[validate_report_extension],
        blank=True,
        null=True
        )
    local = models.CharField(_('local'), blank=True, max_length=120)
    machine = models.CharField(_('machine'), blank=True, max_length=120, default='')

    class meta:
        verbose_name = _('Income')
        verbose_name_plural = _('Incomes')

    def __str__(self):
        return self.invoice_number

    def get_absolute_url(self):
        return reverse('income:income_update', kwargs={'pk': self.pk})
