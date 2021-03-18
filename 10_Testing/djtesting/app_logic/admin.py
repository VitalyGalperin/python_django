from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')
    model = Item


admin.site.register(Item, ItemAdmin)
