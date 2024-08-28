from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {"posts": posts}

    return render(request, "posts/home.html", context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}

    return render(request, "posts/detail.html", context)
