from django.db import models
from django.utils import timezone

# Create your models here.
class H0zzae_Data(models.Model):
    nickname = models.CharField(max_length=20, null=False, verbose_name="닉네임")
    profileText = models.CharField(max_length=200, null=False, verbose_name="자기소개")
    githubUrl=models.URLField(verbose_name="깃허브사이트")
    profileImage = models.ImageField(upload_to='static/image/',blank=True, null=True, verbose_name="프로필사진")
    AdminPassword = models.CharField(max_length=20,null=False,verbose_name="관리자권한번호") #글 작석 및 수정,삭제용

class Category(models.Model):
    name = models.CharField(default="newCategory", max_length=50, null=False, verbose_name = "카테고리 제목")
    def __str__(self):
        return self.name

class Post(models.Model):
    category_num = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "소속 카테고리 번호", related_name='Posts')
    title = models.CharField(max_length=50, null=False, verbose_name = "게시글 제목")
    content = models.TextField(null=False, verbose_name = "게시글 내용")
    created_at = models.DateTimeField(default = timezone.now, verbose_name = "작성시간")
    edited_at = models.DateTimeField(default = timezone.now, verbose_name = "수정시간")
    hit_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    def summary(self):
        return self.content[:100]
    @property
    def update_counter(self):
        self.hit_count = self.hit_count+1
        self.save()

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='static/image/', blank=True, null=True, verbose_name = "첨부파일")

class Reply(models.Model):
    post_num = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="소속 게시글 번호", related_name='Replys')
    userName = models.CharField(max_length=10, verbose_name="댓글작성자")
    content = models.CharField(max_length=200, verbose_name="댓글내용")
    password = models.CharField(default="0000", max_length=4, verbose_name="댓글 비밀번호")
    created_at = models.DateTimeField(default = timezone.now, verbose_name = "댓글작성시간")
