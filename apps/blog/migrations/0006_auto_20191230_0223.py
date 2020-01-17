# Generated by Django 2.2.6 on 2019-12-30 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191230_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='meta_description',
            field=models.CharField(blank=True, max_length=300, verbose_name='meta_description'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=160, verbose_name='meta_keywords'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='meta_title',
            field=models.CharField(blank=True, max_length=60, verbose_name='meta_title'),
        ),
    ]
