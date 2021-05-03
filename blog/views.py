from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body']
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BlogCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'post_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)