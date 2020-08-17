from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from .models import *
from .forms import PostForm

# Create your views here.
def main(request):
    return render(request,'main/main.html')

def postmain(request):
    categorys = Category.objects.all()
    posts = Post.objects.all()

    return render(request,'post/postMain.html', {'categorys': categorys,'posts':posts})

def profile(request):
    return render(request, 'profile/profile.html')

def write(request):
    if request.method=='POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            print("hihi")
        return redirect('/postmain')
    else:
        form = PostForm()
    return render(request, 'post/writePost.html', {'form':form})

def getPost(request):
    posts = Post.objects.all()
    replys = Reply.objects.all()

    return render(request,'post/post.html',{'posts':posts,'replys':replys})
