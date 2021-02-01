from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    contest = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', contest)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<view-type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html', {'title': 'Title Page'})
