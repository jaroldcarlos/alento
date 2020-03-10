
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from easy_thumbnails.fields import ThumbnailerImageField
from core.abstract import ActiveModel


class Worker(ActiveModel):

    user = models.OneToOneField(
        User,
        verbose_name=_('user'),
        related_name='worker',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    image = ThumbnailerImageField(
        _('image'),
        upload_to='worker/',
        default='worker/default.png',
        blank=True
    )

    address = models.CharField(_('address'), max_length=100, blank=True)
    postalcode = models.CharField(_('postal code'), max_length=100, blank=True)
    city = models.CharField(_('city'), max_length=100, blank=True)
    state = models.CharField(_('state'), max_length=100, blank=True)
    dni = models.CharField(_('dni'), max_length=9, unique=True)
    country = models.CharField(_('country'), max_length=100, blank=True)

    phone1 = models.CharField(_('phone'), max_length=100, blank=True)
    phone2 = models.CharField(_('phone'), max_length=100, blank=True)

    contact_name = models.CharField(_('contact name'), max_length=100, blank=True)
    contact_phone = models.CharField(_('contact phone'), max_length=100, blank=True)
    contact_email = models.EmailField(_('contact email'), max_length=100, blank=True)

    note = models.TextField(_('note'), blank=True, null=True)
    private_comment = models.TextField(_('private comment'), blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    def full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    def get_view_url(self):
        return reverse('dashboard:view_worker', kwargs={'dni': self.dni})
