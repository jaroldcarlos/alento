import inspect

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from easy_thumbnails.fields import ThumbnailerImageField

from .managers import ActiveManager, PublishedManager, ReadOnlyManager, InSeasonManager


def image_path(instance, filename):
    path = 'images'
    print(inspect.stack()[1])
    return path


class ActiveModel(models.Model):
    """
    An abstract base class model that provides
    ``active`` field and a manager class.
    """
    active_status = models.BooleanField(_('active_status'), default=False)

    date_active_ini = models.DateField(_('date ini'), null=True, blank=True)
    date_active_end = models.DateField(_('date end'), null=True, blank=True)

    objects = models.Manager()
    actives = ActiveManager()

    @property
    def active(self):
        if not self.active_status == 'p':
            return False

        if self.date_active_ini and self.date_active_ini > timezone.now():
            return False

        if self.date_active_end and self.date_active_end < timezone.now():
            return False

        return True

    class Meta:
        abstract = True


class BuyableModel(models.Model):
    requirements = models.TextField(
        _('requirements'),
        blank=True,
        null=True
        )
    price = models.DecimalField(_('price'), max_digits=5, decimal_places=2, blank=True, null=True)
    link = models.CharField(_('link'), blank=True, null=True, max_length=255)

    @property
    def free(self):
        return True if self.price == 0 else False

    class Meta:
        abstract = True


class CapacityModel(models.Model):
    min_people = models.CharField(
        _('min people'),
        blank=True,
        null=True,
        max_length=120
    )
    max_people = models.CharField(
        _('max people'),
        blank=True,
        null=True,
        max_length=120
    )

    class Meta:
        abstract = True


class ContactModel(models.Model):
    first_name = models.CharField(_('first name'), max_length=160, blank=True)
    last_name = models.CharField(_('last name'), blank=True, max_length=80)
    company = models.CharField(_('company'), blank=True, max_length=80)
    phone = models.CharField(_('phone'), blank=True, max_length=80)
    email = models.CharField(_('email'), blank=True, max_length=80)
    address = models.CharField(_('address'), blank=True, max_length=80)

    @property
    def full_name(self):
        return "{first_name} {last_name}".format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    def __str__(self):
        return '{fist_name}'.format(fist_name=self.first_name)

    class Meta:
        abstract = True


class DescriptionModel(models.Model):
    description_short = models.TextField(
        _('description short'),
        blank=True
    )
    description = models.TextField(
        _('description'),
        blank=True
    )

    def get_description_short(self, num_chars=245):
        if self.description_short:
            if len(self.description_short) > num_chars:
                return self.description_short[:num_chars] + '...'
            else:
                return self.description_short
        else:
            if len(self.description) > num_chars:
                return self.description[:num_chars] + '...'
            else:
                return self.description

    class Meta:
        abstract = True


class GaleryModel(models.Model):
    image1_name = models.CharField(
        '{} 1'.format(_('image name')),
        max_length=50,
        blank=True
    )
    image1 = ThumbnailerImageField(
        '{} 1'.format(_('image')),
        upload_to='Galery/'
    )

    image2_name = models.CharField(
        '{} 2'.format(_('image name')),
        max_length=50,
        blank=True
    )
    image2 = ThumbnailerImageField(
        '{} 2'.format(_('image')),
        upload_to='Galery/'
    )

    image3_name = models.CharField(
        '{} 3'.format(_('image name')),
        max_length=50,
        blank=True
    )
    image3 = ThumbnailerImageField(
        _('image 3'),
        upload_to='Galery/'
    )

    image4_name = models.CharField(
        '{} 4'.format(_('image name')),
        max_length=50,
        blank=True
    )
    image4 = ThumbnailerImageField(
        _('image 4'),
        upload_to='Galery/'
    )

    image5_name = models.CharField(
        '{} 5'.format(_('image name')),
        max_length=50,
        blank=True
    )
    image5 = ThumbnailerImageField(
        _('image 5'),
        upload_to='Galery/'
    )

    image6_name = models.CharField(
        '{} 6'.format(_('image name')),
        max_length=50,
        blank=True
    )
    image6 = ThumbnailerImageField(
        _('image 6'),
        upload_to='Galery/'
    )

    image7_name = models.CharField(
        '{} 7'.format(_('image name')),
        max_length=50,
        blank=True
    )
    image7 = ThumbnailerImageField(
        _('image 7'),
        upload_to='Galery/'
    )

    image8_name = models.CharField(
        '{} 8'.format(_('image name')),
        max_length=50,
        blank=True
    )
    image8 = ThumbnailerImageField(
        _('image 8'),
        upload_to='Galery/'
    )

    def images(self):
        return [
            [self.image1_name, self.image1],
            [self.image2_name, self.image2],
            [self.image3_name, self.image3],
            [self.image4_name, self.image4],
            [self.image5_name, self.image5],
            [self.image6_name, self.image6],
            [self.image7_name, self.image7],
            [self.image8_name, self.image8],
        ]

    class Meta:
        abstract = True


class GeoModel(models.Model):
    latitude = models.CharField(_('latitude'), blank=True, max_length=40)
    longitude = models.CharField(_('longitude'), blank=True, max_length=40)

    def coordinates(self):
        return '{latitude}, {longitude}'.format(
            latitude=self.latitude,
            longitude=self.longitude
        )

    class Meta:
        abstract = True

class HookModel(models.Model):
    HOOK_CHOICES = [
        ('hf', _('home frontend')),
        ('ff', _('footer frontend')),
        ('hd', _('home dashboard')),
        ('fd', _('footer dashboard')),
    ]
    hook = models.CharField(_('hook'), unique=True, blank=True, null=True, max_length=200, choices=HOOK_CHOICES, default='')

    class Meta:
        abstract = True


class IterableModel(models.Model):
    def __iter__(self):
        field_names = [f.name for f in self._meta.fields]
        for field_name in field_names:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def show(self):
        for f in self:
            print(f)

    class Meta:
        abstract = True


class LoginModel(models.Model):
    user = models.CharField(_('user'), max_length=50, blank=True)
    password = models.CharField(_('password'), max_length=100, blank=True)
    url = models.CharField(_('url'), max_length=300, blank=True)

    class Meta:
        abstract = True


class NameModel(models.Model):
    name = models.CharField(_('name'), max_length=200, default="", blank=True)
    # comment = models.TextField(_('comment'), null=True, blank=True, default="")

    def __str__(self):
        return '{name}'.format(name=self.name)

    class Meta:
        abstract = True


class PaymentModel(models.Model):
    date = models.DateField(_('date'))
    date_payment = models.DateField(_('date payment'), blank=True, null=True)

    invoice_number = models.CharField(_('invoice number'), max_length=50, default="", blank=True)
    total = models.DecimalField(_('total'), max_digits=20, decimal_places=6)
    comment = models.TextField(_('comment'), null=True, blank=True, default="")

    # objects = models.Manager()
    # actives = ActivesManager()

    def __str__(self):
        return '{invoice_number} ({total})'.format(
            invoice_number=self.invoice_number,
            total=self.total
        )

    class Meta:
        abstract = True
        # ordering = ('name',)


class PeriodicityModel(models.Model):
    UNIQUE = 'U'
    ANNUAL = 'A'
    BIANUAL = 'B'
    QUATERLY = 'Q'
    MONTHLY = 'M'
    WEEKLY = 'W'
    PERIODICITY_CHOICES = (
        (UNIQUE, 'Puntual'),
        (ANNUAL, 'Anual'),
        (BIANUAL, 'Semestral'),
        (QUATERLY, 'Trimestral'),
        (MONTHLY, 'Mensual'),
        (WEEKLY, 'Semanal'),
    )
    periodicity = models.CharField(
        max_length=1,
        choices=PERIODICITY_CHOICES,
        default=MONTHLY,
    )

    class Meta:
        abstract = True


class PublicityModel(models.Model):
    image = models.FileField(
        _('image'),
        upload_to='publicity/',
        null=True,
        blank=True
    )
    price = models.DecimalField(_('price'), max_digits=20, decimal_places=6)
    link = models.CharField(_('link'), max_length=160, blank=True)

    class Meta:
        abstract = True


class PublishedModel(models.Model):
    STATUS_CHOICES = [
        ('f', _('Form Draft')),
        ('d', _('Draft')),
        ('p', _('Published')),
        ('w', _('Withdrawn')),
    ]

    published_at = models.DateTimeField(null=True, blank=True)
    expired_at = models.DateTimeField(null=True, blank=True)
    publication_status = models.CharField(_('publication status'), max_length=1, choices=STATUS_CHOICES, default='d')  # si la zona es seleccionable o no

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        abstract = True

    @property
    def published_status(self):
        extra = ""
        if self.publication_status == 'p':
            if self.published_at != None and self.published_at > timezone.now():
                extra ='['+_('se mostrará a partir del {date}').format(
                    date=self.published_at,)+']'
            if self.expired_at != None and self.expired_at < timezone.now():
                extra ='['+_('oculto desde el {date}').format(
                    date=self.expired_at,)+']'

        return '{status} {extra}'.format(
            status=self.get_publication_status_display(),
            extra=extra
        )


class ReadOnlyModel(models.Model):
    objects = ReadOnlyManager()  # The ReadOnly manager.

    def save(self, *args, **kwargs):
        pass
        # raise NotImplemented

    def delete(self, *args, **kwargs):
        pass

    class Meta:
        managed = False
        abstract = True


class SeasonModel(models.Model):
    season = models.CharField(
        _('season'),
        blank=True,
        null=True,
        max_length=120
        )
    season_date_ini = models.DateField(
        _('season date ini'),
        blank=True,
        null=True
        )
    season_date_end = models.DateField(
        _('season date end'),
        blank=True,
        null=True
        )
    schedule = models.CharField(
        _('schedule'),
        blank=True,
        null=True,
        max_length=40
        )

    objects = models.Manager()
    in_season = InSeasonManager()

    @property
    def in_season(self):
        if self.season_ini and self.season_ini > timezone.now():
            return False
        if self.season_end and self.season_end < timezone.now():
            return False
        return True

    class Meta:
        abstract = True


class SeoModel(models.Model):
    meta_keywords = models.CharField(_('meta_keywords'), max_length=160, blank=True)
    meta_title = models.CharField(_('meta_title'), max_length=60, blank=True)
    meta_description = models.TextField(_('meta_description'), blank=True)

    class Meta:
        abstract = True


class SlugModel(models.Model):
    slug = models.SlugField(_('slug'), unique=True, null=True, max_length=200, blank=True)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
