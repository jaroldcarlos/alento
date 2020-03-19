# Generated by Django 2.2.6 on 2020-01-22 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0007_worker_dni'),
        ('patient', '0009_auto_20200121_2248'),
        ('schedule', '0011_auto_20200113_1315'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('worker', 'patient', 'date', 'start_time', 'end_time')},
        ),
    ]