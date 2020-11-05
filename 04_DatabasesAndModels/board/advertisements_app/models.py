from datetime import datetime, timedelta

from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField(default='', null=True, verbose_name='Описание')
    price = models.FloatField(null=True, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    advertisement_status = models.ForeignKey('Status', default=None, null=True, on_delete=models.CASCADE,
                                             related_name='ad_status')
    advertisement_type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                                           related_name='ad_type')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Status(models.Model):
    advertisement_status = models.CharField(max_length=20)

    def __str__(self):
        return self.advertisement_status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class AdvertisementType(models.Model):
    advertisement_type = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.advertisement_type


class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    email = models.EmailField
