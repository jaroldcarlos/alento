# Generated by Django 2.2.4 on 2019-11-15 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0006_income_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='machine',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='machine'),
        ),
    ]