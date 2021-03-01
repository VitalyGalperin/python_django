from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.FileField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Аватар')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Аватар пользователя'
        verbose_name_plural = 'Аватары пользователя'
