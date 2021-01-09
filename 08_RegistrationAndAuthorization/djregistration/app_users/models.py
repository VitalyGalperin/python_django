from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    city = models.CharField(max_length=30, blank=True, verbose_name='Город')
    phone = models.CharField(max_length=13, blank=True, verbose_name='Телефон')
    is_verified = models.BooleanField(default=False, verbose_name='Верифицирован')
    news_numbers = models.IntegerField(default=0, verbose_name='Опубликовано новостей')

    class Meta:
        verbose_name = 'Дополнение пользователя'
        verbose_name_plural = 'Дополнения пользователя'
