from django.shortcuts import render
from django.views import generic
from .models import Post

class IndexView(generic.ListView):
    model=Post
