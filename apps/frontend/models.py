from django.db import models


from django.utils.translation import ugettext as _

from mptt.models import MPTTModel, TreeForeignKey
from django.utils.safestring import mark_safe

from core.abstract import (
    ActiveModel,
    DescriptionModel,
    GeoModel,
    HookModel,
    NameModel,
    SeoModel,
    SlugModel,
)


class CategoryLink(DescriptionModel, NameModel, HookModel):

    class meta:
        verbose_name = _('category link')
        verbose_name_plural = _('category links')


class Link(MPTTModel, DescriptionModel, HookModel, NameModel):

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE, default='')
    icon = models.CharField(_('icon'), blank=True, null=True, max_length=40)
    url = models.CharField(_('url'), blank=True, null=True, max_length=120)
    color = models.CharField(_('color'), blank=True, null=True, max_length=40)
    category = models.OneToOneField(
        CategoryLink,
        verbose_name=_('category'),
        related_name='link',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def show(self, title=False):
        descendants = self.get_descendants()
        menu = '<ul class="menu vertical medium-horizontal expanded medium-text-center" data-responsive-menu="drilldown medium-dropdown">'
        if title and self.name:
            menu += '<li class="has-submenu"><a href="{url}">{name}</a></li>'.format(url=self.url, name=self.name)
        for item in descendants:
            menu += '<ul class="submenu menu vertical" data-submenu>'
            menu += "<li class='has-submenu'><a href='{url}'>{name}</a>".format(
                color=item.color,
                url=item.url,
                name=item.name.capitalize()
            )
            menu += '</ul>'
        menu += '</ul>'

        return mark_safe(menu)

    @property
    def full_display_admin(self):
        text = self.name
        if self.hook:
            text += ' [ {} ]'.format(self.hook)
        if self.description:
            text += ' ( {} )'.format(self.description)
        return text

    class MPTTMeta:
        order_insertion_by = ['name']

    class meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')


class Contact_us(NameModel, GeoModel):

    email = models.CharField(_('email'), blank=True, null=True, max_length=40)
    phone = models.CharField(_('phone'), blank=True, null=True, max_length=40)
    address = models.CharField(_('address'), blank=True, null=True, max_length=40)


class Social(ActiveModel):
    FACEBOOK = 'fa fa-facebook'
    INSTAGRAM = 'fa fa-instagram'
    LINKEDIN = 'fa fa-linkedin'
    TWITTER = 'fa fa-twitter'
    PINTEREST = 'fa fa-pinterest-square'
    YOUTUBE = 'fa fa-youtube'
    GOOGLE = 'fa fa-google-plus'

    SOCIAL_CHOICES = [
        (FACEBOOK, 'Facebbok'),
        (INSTAGRAM, 'Instagram'),
        (TWITTER, 'Twitter'),
        (PINTEREST, 'Pinterest'),
        (GOOGLE, 'Google'),
        (LINKEDIN, 'Linkedin'),
    ]

    name = models.CharField(_('network'), max_length=160, blank=True, choices=SOCIAL_CHOICES)
    url = models.CharField(_('url'), max_length=160, blank=True)

    class meta:
        verbose_name = _('Social')
        verbose_name_plural = _('Social')
