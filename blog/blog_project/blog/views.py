from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.
class PostListView(ListView):
    model=Post
    template_name ='home.html'
    context_object_name = 'all_posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail_post.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['author','title', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    context_object_name = 'post'


    