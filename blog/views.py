from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post;

# Create your views here.
posts = [
    {
        'author': 'Khokon',
        'title': 'First post',
        'description': 'First post description',
        'date_posted': 'November 20, 2020'
    },
    {
        'author': 'Kartic',
        'title': 'Second post',
        'description': 'Second post description',
        'date_posted': 'November 22, 2020'
    }
]

def home(request):
    contest = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', contest)

def about(request):
    return render(request, 'blog/about.html', {'title': 'Title Page'})
