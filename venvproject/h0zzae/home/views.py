from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from .models import *
from .forms import PostForm,ReplyForm

# Create your views here.
def main(request):
    NewPost = Post.objects.last()
    RecommendPost = Post.objects.last()
    return render(request,'main/main.html',{'newPost':NewPost,'recommendPost':RecommendPost})

def postmain(request):
    categorys = Category.objects.all()
    posts = Post.objects.all()

    return render(request,'post/postMain.html', {'categorys': categorys,'posts':posts})

def profile(request):
    return render(request, 'profile/profile.html')

def write(request):
    category = Category.objects.all()
    selectedCategory = Category()
    if request.method=='POST':
        post = Post()
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.created_at = timezone.datetime.now()
            selectedCategory.id = request.POST['categorys']
            post.category_num = selectedCategory
            post.save()
            for img in request.FILES.getlist('images'):
                photo = Photo()
                photo.post = post
                photo.image = img
                photo.save()
        return redirect('/post/')
    else:
        form = PostForm()

    return render(request, 'post/writePost.html', {'form':form, 'categorys':category})

def getPost(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        reply_form.instance.post_num_id = post_id
        if reply_form.is_valid():
            replyform = reply_form.save()

    reply_form = ReplyForm()
    Replys = post.Replys.all()
    return render(request, 'post/detail.html', {'post': post, 'replys': Replys, 'reply_form': reply_form})

def getCategory(request,category_id):
    category = get_object_or_404(Category, pk=category_id)

    posts = category.Posts.all()
    return render(request, 'post/categoryPost.html',{'category':category,'posts':posts})

def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/post')

def replyDelete(request,reply_id,post_id):
    reply = Reply.objects.get(id=reply_id)
    reply.delete()

    return redirect('/post/'+str(post_id))

def editPost(request, post_id):
    category = Category.objects.all()
    post = Post.objects.get(id=post_id)

    if request.method =='POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.edited_at = timezone.datetime.now()
            post.save()
            for img in request.FILES.getlist('images'):
                photo = Photo()
                photo.post = post
                photo.image = img
                photo.save()
        return redirect('/post/'+str(post_id))
    else:
        form = PostForm(instance=post)

    return render(request, 'post/editPost.html', {'form': form})
