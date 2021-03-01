from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=150, default='', verbose_name='Название')
    description = models.TextField(default='', null=True, verbose_name='Запись')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликована')
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE,
                             related_name='creator_link')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def get_absolute_url(self):
        return reverse('/', kwargs={'pk': self.pk})


class Images(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Иллюстрация')
    blog = models.ForeignKey(Blog, default=None, null=True, blank=True, on_delete=models.CASCADE,
                             related_name='image_link')

    class Meta:
        verbose_name = 'Иллюстрация'
        verbose_name_plural = 'Иллюстрации'
