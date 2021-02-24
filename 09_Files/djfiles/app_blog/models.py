from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Images(models.Model):
    image = models.FileField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Иллюстрация')

    class Meta:
        verbose_name = 'Иллюстрация'
        verbose_name_plural = 'Иллюстрации'


class Blog(models.Model):
    title = models.CharField(max_length=150, default='', verbose_name='Название')
    description = models.TextField(default='', null=True, verbose_name='Запись')
    images = models.ForeignKey(Images, default=None, null=True, blank=True, on_delete=models.CASCADE,
                               related_name='image_link')
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE,
                             related_name='creator_link')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def get_absolute_url(self):
        return reverse('/', kwargs={'pk': self.pk})
