# Generated by Django 2.2.4 on 2019-09-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='total'),
        ),
    ]
