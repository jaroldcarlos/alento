# Generated by Django 2.2.6 on 2020-01-01 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20200101_0331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='phone1',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone2',
        ),
    ]
