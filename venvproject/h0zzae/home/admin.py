from django.contrib import admin
from .models import Category, Post, Reply

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Reply)
