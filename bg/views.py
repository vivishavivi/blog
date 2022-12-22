from django.shortcuts import render, redirect
from . models import Post
from . forms import MakePost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    post = {
        'post':Post.objects.all()
    }
    return render(request, 'index.html',post)
def post(request, post_id):
    post = {
        'post':Post.objects.get(id=post_id)
    }
    return render(request, 'post.html',post)
def make(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request, 'make.html',{'form':MakePost()})
    
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return index(request)
def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    form = MakePost(instance=post)
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit.html', {'form': form})
@login_required
def create(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('index')
    return render(request, 'create.html',{'form':MakePost()})
def register(request):
    form = UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
    return render(request,'register.html',{'form':form})





