from django.contrib import admin
from .models import Category, Post, Reply, Photo, H0zzae_Data

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Reply)
admin.site.register(H0zzae_Data)