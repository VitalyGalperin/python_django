from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    count_of_employers = models.IntegerField(verbose_name='Кол-во работников')
    director = models.CharField(max_length=30, verbose_name='Директор')
    chef = models.CharField(max_length=30, verbose_name='Шеф-повар')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    country = models.CharField(max_length=30, verbose_name='Страна')
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=30, verbose_name='Улица')
    house = models.IntegerField(verbose_name='№ дома')
    serves_hot_dogs = models.BooleanField(default=False, verbose_name='Есть ли хот-доги')
    serves_pizza = models.BooleanField(default=False, verbose_name='Есть ли пицца')
    serves_sushi = models.BooleanField(default=False, verbose_name='Есть ли суши')
    serves_burgers = models.BooleanField(default=False, verbose_name='Есть ли бургеры')
    serves_coffee = models.BooleanField(default=False, verbose_name='Есть ли кофе')
    serves_donats = models.BooleanField(default=False, verbose_name='Есть ли донаты')

    def __str__(self):
        return f'{self.name} ({self.city})'

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'


class Waiter(models.Model):
    SEX = [('М', 'Мужчина'), ('Ж', 'Женщина')]
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='Ресторан')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    sex = models.CharField(max_length=1, choices=SEX, verbose_name='Пол')
    country = models.CharField(max_length=30, verbose_name='Страна')
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=30, verbose_name='Улица')
    house = models.IntegerField(verbose_name='Дом')
    apartment = models.IntegerField(verbose_name='Квартира')
    seniority = models.TextField(verbose_name='Стаж')
    education = models.TextField(max_length=50, verbose_name='Образование')
    cources = models.TextField(max_length=50, verbose_name='Курсы')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Официант'
        verbose_name_plural = 'Официанты'
