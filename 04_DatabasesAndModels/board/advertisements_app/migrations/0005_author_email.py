# Generated by Django 2.2 on 2020-11-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0004_auto_20201109_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='+7', max_length=254),
        ),
    ]
