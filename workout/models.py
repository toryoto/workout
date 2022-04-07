from pyexpat import model
from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class Place(models.Model):
    title = models.CharField(
        verbose_name ='カテゴリ1',
        max_length = 20,
    )

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(
        verbose_name ='カテゴリ2',
        max_length = 20,
    )

    def __str__(self):
        return self.title



class WorkoutPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name = 'ユーザー',
        on_delete = models.CASCADE,
    )

    place = models.ForeignKey(
        Place,
        verbose_name = 'カテゴリ1',
        on_delete = models.PROTECT,
    )

    category = models.ForeignKey(
        Category,
        verbose_name = 'カテゴリ2',
        on_delete = models.PROTECT
    )
    
    title = models.CharField(
        verbose_name = 'タイトル',
        max_length = 200,
    )

    content = models.TextField(
        verbose_name = '本文',
    )

    image1 = models.ImageField(
        verbose_name = 'イメージ１',
        upload_to = 'photos',
    )

    posted_at = models.DateTimeField(
        verbose_name = '投稿日時',
        auto_now_add = True,
    )

    updated_at = models.DateTimeField(
        verbose_name = '更新日時',
        auto_now_add = True,
    )

class Comment(models.Model):
    target = models.ForeignKey(WorkoutPost, on_delete=models.CASCADE, verbose_name='対象記事')
    text = models.TextField('本文')