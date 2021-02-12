# Generated by Django 2.2 on 2021-01-28 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Город')),
                ('phone', models.CharField(blank=True, max_length=13, verbose_name='Телефон')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Верифицирован')),
                ('news_number', models.IntegerField(default=0, verbose_name='Опубликовано новостей')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Дополнение пользователя',
                'verbose_name_plural': 'Дополнения пользователя',
                'permissions': (('can_verified_users', 'Может верифицировать пользователей'), ('can_publish', 'Может публиковать'), ('can_view_unverified', 'Видеть неверифицированные новости')),
            },
        ),
    ]