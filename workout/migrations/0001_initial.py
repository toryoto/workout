# Generated by Django 3.2.4 on 2022-01-30 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='カテゴリ2')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='カテゴリ1')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='本文')),
                ('image1', models.ImageField(upload_to='photos', verbose_name='イメージ１')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('like', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workout.category', verbose_name='カテゴリ2')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workout.place', verbose_name='カテゴリ1')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='workout.workoutpost')),
            ],
        ),
    ]