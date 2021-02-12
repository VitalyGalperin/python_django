from django.db import models


class Item(models.Model):
    # name = models.CharField(max_length=100, verbose_name='название')
    code = models.CharField(max_length=100, verbose_name='артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class File(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
