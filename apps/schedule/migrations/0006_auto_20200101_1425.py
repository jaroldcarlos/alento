# Generated by Django 2.2.6 on 2020-01-01 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20200101_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='patient.Patient', verbose_name='patient'),
        ),
        migrations.AlterField(
            model_name='event',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='worker.Worker', verbose_name='worker'),
        ),
    ]
