from tokenize import Comment
from django.contrib import admin
from setuptools import Command
from .models import Place, Category, WorkoutPost, Comment

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class WorkoutPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(WorkoutPost, WorkoutPostAdmin)