# Generated by Django 2.2 on 2021-01-13 11:38

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
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='', max_length=150, verbose_name='Название')),
                ('description', models.TextField(default='', null=True, verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликована')),
                ('edit_at', models.DateTimeField(auto_now=True, verbose_name='Изменена')),
                ('is_active', models.BooleanField(default=False, null=True, verbose_name='Активна')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Teg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teg', models.CharField(blank=True, max_length=15, null=True, verbose_name='Тег')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликована')),
                ('news', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_news.NewsItem')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='', null=True, verbose_name='Комментарий')),
                ('user_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя пользователя')),
                ('news_fk', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_link', to='app_news.NewsItem')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_link', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
