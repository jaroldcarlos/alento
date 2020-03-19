# Generated by Django 2.2.4 on 2019-11-14 17:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0007_auto_20191114_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='id',
        ),
        migrations.AlterField(
            model_name='expense',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]