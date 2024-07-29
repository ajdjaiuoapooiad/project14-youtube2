from django.shortcuts import render,redirect
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from .forms  import PostCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

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
    
def signupfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request,'youtube/signup.html',{'error':'このユーザーはすでに使用されています'})
        except:
            user = User.objects.create_user(username2, "", password2)
            return redirect('youtube:index')
    return render(request,'youtube/signup.html',{'some':100})

def loginfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        user = authenticate(username=username2, password=password2)
        if user is not None:
            login(request,user)
            return redirect('youtube:index')
        else:
            return render(request,'youtube/signup.html',{'error':'登録されていません'})
        
    
    return render(request,'youtube/login.html')