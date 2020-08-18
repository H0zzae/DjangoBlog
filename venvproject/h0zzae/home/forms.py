from django.forms import ModelForm
from .models import Post,Reply

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','attach']

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['userName','content','password']