from dataclasses import field
from multiprocessing import context
from re import template
from turtle import right
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from matplotlib.collections import PathCollection
from numpy import place

import workout
from .forms import WorkoutPostForm, CommentForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import WorkoutPost, Comment
from django.http import Http404, HttpResponse
from django.http.response import JsonResponse
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64

class IndexView(ListView):
    template_name = 'index.html'
    queryset = WorkoutPost.objects.order_by('-posted_at')
    paginate_by = 4

#デコレーターによりCreateViewへのアクセスはログインユーザーに限定される。
@method_decorator(login_required, name='dispatch')
class CreateWorkoutView(CreateView):
    form_class = WorkoutPostForm
    template_name = 'post.html'
    success_url = reverse_lazy('workout:post_done')

    def form_valid(self, form):
        #フォームのバリデーションを通過したときに呼ばれる.
        #フォームデータの登録をここで行ってる！
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_done.html'

class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 4

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = WorkoutPost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list


class DetailView(DetailView):
    template_name = 'detail.html'
    model = WorkoutPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートにコメント作成フォームを渡す
        context['comment_form'] = CommentForm

        return context

class Comment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        post = get_object_or_404(WorkoutPost, pk=pk)
        #post = WorkoutPost.objects.get(id=pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        #return super().form_valid(form)
        return redirect('workout:workout_detail', pk=pk)

    


class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = WorkoutPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

    
class WorkoutDeleteView(DeleteView):
    model = WorkoutPost
    template_name = 'delete.html'
    success_url = reverse_lazy('workout:mypage')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class WorkoutUpdateView(UpdateView):
    model = WorkoutPost
    template_name = 'edit.html'
    fields = ('title', 'category', 'place', 'content', 'image1')
    success_url = reverse_lazy('workout:index')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.updated_at = timezone.now()
        postdata.save()
        return super().form_valid(form)


def get_place_svg(request):

    def make_chart(x, y):
        plt.bar(x, y, color='#00d5ff')
        plt.xlabel('Place')
        plt.ylabel('Amounts')
    
    def convert_to_svg():
        buffer = io.BytesIO()
        plt.savefig(buffer, format='svg', bbox_inches='tight')
        s = buffer.getvalue()
        buffer.close()
        return s

    A = 0
    G = 0
    J = 0
    O = 0
    for postdata in WorkoutPost.objects.all():
        if postdata.place_id == 1:
            A += 1;
        if postdata.place_id == 2:
            G += 1;
        if postdata.place_id == 3:
            J += 1;
        if postdata.place_id == 4:
            O += 1;

    x = ['Anytime Fitness', 'Gold Gym', 'Joy Fit', 'Other']
    y = [A, G, J, O]

    make_chart(x, y)

    svg = convert_to_svg()
    plt.cla()
    
    return HttpResponse(svg, content_type='image/svg+xml')

def data_screen(request):
    return render(request, 'data.html')

