# Generated by Django 2.2 on 2021-03-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_auto_20210228_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/', verbose_name='Иллюстрация'),
        ),
    ]
