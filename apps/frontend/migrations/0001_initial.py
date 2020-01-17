# Generated by Django 2.2.7 on 2019-12-25 12:35

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_short', models.TextField(blank=True, verbose_name='description short')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('hook', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='hook')),
                ('name', models.CharField(blank=True, default='', max_length=200, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_short', models.TextField(blank=True, verbose_name='description short')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('hook', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='hook')),
                ('name', models.CharField(blank=True, default='', max_length=200, verbose_name='name')),
                ('icon', models.CharField(blank=True, max_length=40, null=True, verbose_name='icon')),
                ('url', models.CharField(blank=True, max_length=40, null=True, verbose_name='url')),
                ('color', models.CharField(blank=True, max_length=40, null=True, verbose_name='color')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='frontend.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
