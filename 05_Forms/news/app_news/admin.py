from django.contrib import admin
from .models import NewsItem, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active',)
    exclude = ('description',)
    inlines = (CommentInLine,)
    actions = ('mark_as_active', 'mark_as_inactive')

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)

    mark_as_active.short_description = 'Перевести в статус "Активно"'
    mark_as_inactive.short_description = 'Перевести в статус "Не Активно"'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment')
    list_filter = ('user',)
    search_fields = ('user',)
    actions = ('deleted_by_admin',)

    def deleted_by_admin(self, request, queryset):
        queryset.update(comment='Удалено администратором')

    deleted_by_admin.short_description = 'Перевести в статус "Удалено администратором"'


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(Comment, CommentAdmin)

