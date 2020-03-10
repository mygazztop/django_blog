from django.shortcuts import render
from django.http import HttpResponse
import random
from django_blog.apps.my_blog.models import Post, Author


def index(request):
    post_list = Post.objects.all()
    context = {'posts': post_list}
    return render(request, 'index.html', context)


def post(request, id):
    post = Post.objects.get(id=id)
    context = {
        'id': post.id,
        'title': post.title,
        'text': post.text,
        'key_words': post.key_words.all(),
        'author': post.author
    }
    return render(request, 'post.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def contacts(request):
    context = {}
    return render(request, 'contacts.html', context)
