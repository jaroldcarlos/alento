# Generated by Django 2.2.6 on 2020-01-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20200120_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=120, verbose_name='email'),
        ),
    ]
