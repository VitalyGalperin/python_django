from django.db import models


class NewsItem(models.Model):
    title = models.CharField(max_length=150, default='', db_index=True, verbose_name='Название')
    description = models.TextField(default='', null=True, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликована')
    edit_at = models.DateTimeField(auto_now=True, verbose_name='Изменена')
    is_active = models.BooleanField(default=True, null=True, verbose_name='Активна')

    def __str__(self):
        return self.title

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


class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    birthday = models.DateField()
