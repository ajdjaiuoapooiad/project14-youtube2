from django.shortcuts import render,redirect
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from .forms  import PostCreateForm

class IndexView(generic.ListView):
    model=Post
    
class DetailView(generic.DetailView):
    model=Post
    
class CreateView(generic.CreateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('youtube:index')
    
class DeleteView(generic.DeleteView):
    model=Post
    success_url=reverse_lazy('youtube:index')
    
class UpdateView(generic.UpdateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('youtube:index')