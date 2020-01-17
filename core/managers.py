from django.utils import timezone

from django.db.models import Q
from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        objects = super(ActiveManager, self).get_queryset()
        objects = objects.filter(active_status=True)
        objects = objects.filter(
            Q(date_active_ini__isnull=True) |
            (Q(date_active_ini__isnull=False) & Q(date_active_ini__lte=timezone.now()))
        )
        objects = objects.filter(
            Q(date_active_end__isnull=True) |
            (Q(date_active_end__isnull=False) & Q(date_active_end__gt=timezone.now()))
        )
            # objects.filter(date_active_end__gte=timezone.now())
        return objects


class PublishedManager(models.Manager):
    def get_queryset(self):
        objects = super(PublishedManager, self).get_queryset()
        objects = objects.filter(publication_status='p')
        objects = objects.filter(
            Q(published_at__isnull=True) |
            (Q(published_at__isnull=False) & Q(published_at__lte=timezone.now()))
        )
        objects = objects.filter(
            Q(expired_at__isnull=True) |
            (Q(expired_at__isnull=False) & Q(expired_at__gt=timezone.now()))
        )

        return objects


class InSeasonManager(models.Manager):
    def get_queryset(self):
        return super(InSeasonManager, self).get_queryset().filter(
            season_ini__lte=timezone.now(),
            season_end__gte=timezone.now()
        )


class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(
            user__groups__name="user"
        )


class StaffManager(models.Manager):
    def get_queryset(self):
        return super(StaffManager, self).get_queryset().filter(
            user__groups__name="staff"
        )


class AdminManager(models.Manager):
    def get_queryset(self):
        return super(AdminManager, self).get_queryset().filter(
            user__groups__name="admin"
        )


# Read Only Mananger
class ReadOnlyManager(models.Manager):
    def update(self, *args, **kwargs):
        pass
