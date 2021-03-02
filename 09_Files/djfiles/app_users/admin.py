from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)

