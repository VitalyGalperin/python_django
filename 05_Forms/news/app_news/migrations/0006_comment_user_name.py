# Generated by Django 2.2 on 2021-01-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_auto_20210103_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя пользователя'),
        ),
    ]
