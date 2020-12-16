from django.db import models
from django.urls import reverse


class NewsItem(models.Model):
    title = models.CharField(max_length=150, default='', db_index=True, verbose_name='Название')
    description = models.TextField(default='', null=True, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликована')
    edit_at = models.DateTimeField(auto_now=True, verbose_name='Изменена')
    is_active = models.BooleanField(default=True, null=True, verbose_name='Активна')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('/', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    user = models.CharField(max_length=30, verbose_name='Пользователь')
    comment = models.TextField(default='', null=True, verbose_name='Комментарий')
    news_fk = models.ForeignKey('NewsItem', default=None, null=True, on_delete=models.CASCADE,
                                related_name='news_link')

    def __str__(self):
        return self.comment


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


