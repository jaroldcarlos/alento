import uuid
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.abstract import PaymentModel


def validate_report_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(_('Only PDF files allowed'))


class Expense(PaymentModel):
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        related_name='expenses',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    local = models.CharField(_('local'), blank=True, max_length=120)
    invoice_file = models.FileField(
        _('invoice file'),
        upload_to='expenses/',
        validators=[validate_report_extension],
        blank=True,
        null=True
        )
    machine = models.CharField(_('machine'), blank=True, max_length=120, default='')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')

    def __str__(self):
        return self.invoice_number

    def get_absolute_url(self):
        return reverse('expense:expense_update', kwargs={'pk': self.pk})
