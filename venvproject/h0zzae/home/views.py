from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm

# Create your views here.
def main(request):
    return render(request,'main/main.html')

def post(request):
    return render(request,'post/post.html')

def profile(request):
    return render(request, 'profile/profile.html')

def write(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/writePost')
    else:
        form = PostForm()
    return render(request, 'post/writePost.html', {'form':form})