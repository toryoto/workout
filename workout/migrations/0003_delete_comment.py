# Generated by Django 3.2.4 on 2022-02-03 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_remove_workoutpost_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
