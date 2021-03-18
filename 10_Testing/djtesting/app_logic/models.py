from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, default='', verbose_name='название')
    code = models.CharField(max_length=100, verbose_name='артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
