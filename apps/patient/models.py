from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from easy_thumbnails.fields import ThumbnailerImageField
from core.abstract import ActiveModel

from apps.worker.models import Worker


class Patient(ActiveModel):

    worker = models.ForeignKey(
        Worker,
        verbose_name=_('worker'),
        related_name='patient',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    image = ThumbnailerImageField(
        _('image'),
        upload_to='patient/',
        default='patient/default.png',
        blank=True
    )

    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    last_name = models.CharField(_('last name'), max_length=100, blank=True)
    dni = models.CharField(_('dni'), max_length=9, unique=True)

    address = models.CharField(_('address'), max_length=100, blank=True)
    postalcode = models.CharField(_('postal code'), max_length=100, blank=True)
    city = models.CharField(_('city'), max_length=100, blank=True)
    state = models.CharField(_('state'), max_length=100, blank=True)

    country = models.CharField(_('country'), max_length=100, blank=True)

    phone = models.CharField(_('phone'), max_length=100, blank=True)

    contact_name = models.CharField(_('contact name'), max_length=100, blank=True)
    contact_phone = models.CharField(_('contact phone'), max_length=100, blank=True)
    contact_email = models.EmailField(_('contact email'), max_length=100, blank=True)

    note = models.TextField(_('note'), blank=True, null=True)
    private_comment = models.TextField(_('private comment'), blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.first_name)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # def get_absolute_url(self):
    #     return reverse('usuario:view', kwargs={'pk': self.pk})
