# Generated by Django 2.2.7 on 2019-12-28 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_auto_20191228_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='email1',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='passwd',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='staff',
        ),
    ]
