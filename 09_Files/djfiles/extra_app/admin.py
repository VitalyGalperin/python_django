from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    model = Item


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')


admin.site.register(Item, ItemAdmin)
admin.site.register(File, FileAdmin)
