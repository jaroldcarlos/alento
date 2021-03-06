# Generated by Django 2.2.6 on 2019-12-28 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='dni',
            field=models.CharField(blank=True, default='', max_length=9, verbose_name='dni'),
        ),
        migrations.AddField(
            model_name='worker',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='worker',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='worker',
            name='active',
            field=models.BooleanField(default=False, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
