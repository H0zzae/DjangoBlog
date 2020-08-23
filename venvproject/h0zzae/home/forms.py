from django.forms import ModelForm
from .models import Post,Reply

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['userName','content','password']
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = "댓글"