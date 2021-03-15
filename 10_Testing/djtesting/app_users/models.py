from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='avatar_link')
    avatar = models.ImageField(upload_to='images/', blank=True, verbose_name='Аватар')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Аватар пользователя'
        verbose_name_plural = 'Аватары пользователя'
