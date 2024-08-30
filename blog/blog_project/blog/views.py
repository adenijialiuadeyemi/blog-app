from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post
# Create your views here.
class PostListView(ListView):
    model=Post
    template_name ='home.html'
    context_object_name = 'all_posts'

class PostDetailView(DeleteView):
    model = Post
    template_name = 'detail_post.html'
    context_object_name = 'post'
    