from django.contrib import admin
from .models import Restaurant, Waiter


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основные сведения', {
            'fields': ('name', 'description', 'phone')
        }),
        ('Персонал', {
            'fields': ('count_of_employers', 'director', 'chef'),
            'classes': ['collapse']
        }),
        ('Адрес', {
            'fields': ('country', 'city', 'street', 'house'),
            'classes': ['collapse']
        }),
        ('Особенности меню', {
            'fields': ('serves_hot_dogs', 'serves_pizza', 'serves_sushi', 'serves_burgers', 'serves_coffee'),
            'classes': ['collapse']
        }),
        ('Возможность донатов', {
            'fields': ('serves_donats',),
            'classes': ['collapse']
        }),
    )


class WaiterAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Место работы', {
            'fields': ('restaurant',)
        }),
        ('Личные сведения', {
            'fields': ('first_name', 'last_name', 'age', 'sex')
        }),
        ('Адрес', {
            'fields': ('country', 'city', 'street', 'house', 'apartment'),
            'classes': ['collapse']
        }),
        ('Образование и Стаж', {
            'fields': ('seniority', 'education', 'cources'),
            'classes': ['collapse']
        }),
    )


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)




