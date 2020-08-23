from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from .models import *
from .forms import PostForm,ReplyForm

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
        post = Post()
        form = PostForm(request.POST or None, request.FILES or None)
        # form.instance.category_num_id = category_id

        if form.is_valid():
            # post.category_num = form.category_num
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.created_at = timezone.datetime.now()
            post.save()
            for img in request.FILES.getlist('images'):
                photo = Photo()
                photo.post = post
                photo.image = img
                photo.save()
        return redirect('/post/')
    else:
        form = PostForm()

    return render(request, 'post/writePost.html', {'form':form})

def getPost(request,post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        # reply_form.instance.userName_id = request.user.id
        reply_form.instance.post_num_id = post_id
        if reply_form.is_valid():
            replyform = reply_form.save()
    reply_form = ReplyForm()
    Replys = post.Replys.all()
    return render(request, 'post/detail.html', {'post': post, 'replys': Replys, 'reply_form': reply_form})

def getCategory(request,category_id):
    category = get_object_or_404(Category, pk=category_id)

    return render(request, 'post/categoryPost.html',{'category':category})