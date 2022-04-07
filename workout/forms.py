from dataclasses import field
from django.forms import ModelForm, Textarea
from .models import WorkoutPost, Comment

class WorkoutPostForm(ModelForm):
    class Meta:
        model = WorkoutPost
        fields = ['title', 'category', 'place', 'content', 'image1']
        widgets = {
            'content': Textarea(attrs={'cols':30}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']