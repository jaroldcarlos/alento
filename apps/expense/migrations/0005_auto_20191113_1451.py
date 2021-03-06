# Generated by Django 2.2.4 on 2019-11-13 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_auto_20191113_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='local',
            field=models.CharField(blank=True, max_length=120, verbose_name='local'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
