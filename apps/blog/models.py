from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField

from core.abstract import (
    ActiveModel,
    SeoModel,
    SlugModel,
    DescriptionModel
    )


# Create your models here.
class BlogCategory(ActiveModel):
    name = models.CharField(_('name'), max_length=200, null=True, blank=True)
    description_short = models.TextField(_('description short'), null=True, blank=True)
    image = models.ImageField(
        _('image'),
        null=True,
        blank=True,
        upload_to="blogcategory/")

    class meta:
        verbose_name = _('category blog')
        verbose_name_plural = _('categories blogs')

    def __str__(self):
        return '{}'.format(self.name)

    def get_view_url(self):
        return reverse('blog:blog_category', kwargs={'category': self.name})


class BlogPost(ActiveModel, SlugModel, DescriptionModel, SeoModel):

    author = models.CharField(_('author'), max_length=200, null=True, blank=True)
    title = models.CharField(_('title'), max_length=200, null=True, blank=True)
    subtitle = models.CharField(_('subtitle'), max_length=200, null=True, blank=True)
    category = models.ForeignKey(
        BlogCategory,
        related_name='categories',
        on_delete=models.CASCADE
        )
    icon = models.CharField(_('icon'), null=True, blank=True, max_length=200)
    name_image = models.CharField(_('name image'), max_length=200, null=True, blank=True)
    image = ThumbnailerImageField(
        _('image'),
        upload_to='blog/',
        default='blog/default.jpg',
        blank=True
        )

    class meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')

    def __str__(self):
        return '{}'.format(self.title)

    def get_view_url(self):
        return reverse('blog:blog_post', kwargs={'slug': self.slug})
