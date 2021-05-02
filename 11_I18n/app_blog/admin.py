from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('title', 'created_at', 'user')


class ImagesAdmin(admin.ModelAdmin):
    model = Images


admin.site.register(Blog, BlogAdmin)
admin.site.register(Images, ImagesAdmin)