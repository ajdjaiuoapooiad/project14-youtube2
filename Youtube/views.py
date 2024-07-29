from django.shortcuts import render,redirect
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from .forms  import PostCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin,generic.ListView):
    model=Post
    login_url='youtube:login'
    
def detailfunc(request,pk):
    post=Post.objects.get(pk=pk)
    post.read += 1 #閲覧数をインクリメント
    post.save()
    return render(request,'youtube/post_detail.html',{'post':post})
    
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

def logoutfunc(request):
    logout(request)
    return redirect('youtube:index')

def goodfunc(request,pk):
    post=Post.objects.get(pk=pk)
    post2=request.user.get_username()
    if post2 in post.usertext:
        return redirect('youtube:index')
    else:
        post.good+=1
        post.usertext=post.usertext + ' ' + post2
        post.save()
        return redirect('youtube:index')
    
def mypagefunc(request,pk):
    user = User.objects.get(pk=pk)
    return render(request,'youtube/mypage.html')
    
   