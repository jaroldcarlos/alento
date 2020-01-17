# Generated by Django 2.2.6 on 2019-12-29 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191229_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug_en',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug_es',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug_gl',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug_pt',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='slug'),
        ),
    ]
