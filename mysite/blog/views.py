from django.shortcuts import render
from blog.models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_on')
    context={
        "posts":posts,
    }
    return render(request,"blog/index.html",context)

def category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/category.html", context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }

    return render(request, "blog/detail.html", context)