# Generated by Django 2.2.6 on 2020-01-01 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='note'),
        ),
    ]
