from django.contrib import admin
from .models import Category, Post, Reply, Photo

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Reply)