from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.translation import ugettext as _
from core.abstract import (
    ActiveModel,
    DescriptionModel,
    NameModel,
)


# Create your models here.
class CategoryService(
    ActiveModel,
    NameModel,
    DescriptionModel,
):

    image = ThumbnailerImageField(
        _('image'),
        upload_to='category_service/',
        blank=True,
    )

    def __str__(self):
        return '{}'.format(self.name)

    class meta:
        verbose_name = _('category service')
        verbose_name_plural = _('categories services')


class Service(
    ActiveModel,
    NameModel,
    DescriptionModel,
):
    category = models.ForeignKey(
        CategoryService,
        verbose_name=_('category'),
        related_name='service',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    image = ThumbnailerImageField(
        _('image'),
        upload_to='service/',
        blank=True,
    )

    def __str__(self):
        return '{}'.format(self.name)

    class meta:
        verbose_name = _('category service')
        verbose_name_plural = _('categories services')


class SpecialisedUnit(ActiveModel, NameModel):
    image = ThumbnailerImageField(
        _('image'),
        upload_to='SpecialisedUnit/',
        blank=True,
    )

    def __str__(self):
        return '{}'.format(self.name)

    class meta:
        verbose_name = _('Specialised Unit')
        verbose_name_plural = _('Specialised Units')
