from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name = "카테고리 제목")
class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name = "게시글 제목")
    content = models.TextField(verbose_name = "게시글 내용")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "작성시간")
    edited_at = models.DateTimeField(auto_now = True, verbose_name = "수정시간")
    category_num = models.IntegerField(verbose_name = "소속 카테고리 번호")
    attach = models.FileField(null = True, verbose_name = "첨부파일")
class Reply(models.Model):
    userName = models.CharField(max_length=10, verbose_name="댓글작성자")
    content = models.CharField(max_length=200, verbose_name="댓글내용")
    password = models.CharField(max_length=4, verbose_name="댓글 비밀번호")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "댓글작성시간")
    post_num = models.IntegerField(verbose_name="소속 게시글 번호")
