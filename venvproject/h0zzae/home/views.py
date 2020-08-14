from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
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
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            print("hihi")
        return redirect('/post')
    else:
        form = PostForm()
    return render(request, 'post/writePost.html', {'form':form})

def getCategory(request):
    categorys = Category.objects.all()

    return render(request, 'templates/post/post.html', {'categorys':categorys})
def getPost(request):
    posts = Post.objects.all()
    return render(request, 'post/post.html',{'posts':posts})