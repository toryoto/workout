# Generated by Django 3.2.4 on 2022-04-05 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0010_auto_20220406_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='article',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]