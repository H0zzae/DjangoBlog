from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class Category(models.Model):
    name = models.CharField(default="newCategory", max_length=50, null=False, verbose_name = "카테고리 제목")
    def __str__(self):
        return self.name

class Post(models.Model):
    # category_num = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "소속 카테고리 번호")
    title = models.CharField(max_length=50, null=False, verbose_name = "게시글 제목")
    content = models.TextField(null=False, verbose_name = "게시글 내용")
    created_at = models.DateTimeField(default = timezone.now, verbose_name = "작성시간")
    edited_at = models.DateTimeField(default = timezone.now, verbose_name = "수정시간")
    attach = models.ImageField(upload_to ="h0zzae/h0zzae/static/image", null=False, default="", verbose_name = "첨부파일")
    def __str__(self):
        return self.title

class Reply(models.Model):
    post_num = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="소속 게시글 번호")
    userName = models.CharField(max_length=10, verbose_name="댓글작성자")
    content = models.CharField(max_length=200, verbose_name="댓글내용")
    password = models.CharField(max_length=4, verbose_name="댓글 비밀번호")
    created_at = models.DateTimeField(default = timezone.now, verbose_name = "댓글작성시간")

class HitCount(models.Model):
    ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None, null=True)  # 게시글 Foreign Key on_delete=필수
    date = models.DateField(default=timezone.now, null=True, blank=True)  # 조회수가 올라갔던 날짜