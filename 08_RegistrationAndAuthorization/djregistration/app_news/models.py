from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Tag(models.Model):

    tag = models.CharField(max_length=25, blank=True, null=True, verbose_name='Тег')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликована')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        return reverse('/', kwargs={'pk': self.pk})


class NewsItem(models.Model):
    title = models.CharField(max_length=150, default='', db_index=True, verbose_name='Название')
    description = models.TextField(default='', null=True, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликована')
    edit_at = models.DateTimeField(auto_now=True, verbose_name='Изменена')
    is_active = models.BooleanField(default=False, null=True, blank=True, verbose_name='Активна')
    tag = models.ManyToManyField(Tag, null=True, blank=True, verbose_name='Теги')
    creator = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='creator_link')

    def __str__(self):
        return self.title
    #
    # def get_absolute_url(self):
    #     return reverse('/', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    comment = models.TextField(default='', null=True, verbose_name='Комментарий')
    user_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя пользователя')
    news_fk = models.ForeignKey('NewsItem', default=None, null=True, on_delete=models.CASCADE,
                                related_name='news_link')
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE, related_name='user_link')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



