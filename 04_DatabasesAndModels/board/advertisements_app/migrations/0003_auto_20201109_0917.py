# Generated by Django 2.2 on 2020-11-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0002_remove_advertisement_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status',
            new_name='Heading',
        ),
        migrations.RenameModel(
            old_name='AdvertisementType',
            new_name='Type',
        ),
        migrations.AlterModelOptions(
            name='heading',
            options={'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
        migrations.RenameField(
            model_name='advertisement',
            old_name='advertisement_status',
            new_name='advertisement_heading',
        ),
        migrations.RenameField(
            model_name='advertisement',
            old_name='update_at',
            new_name='finish_at',
        ),
        migrations.AddField(
            model_name='author',
            name='phone',
            field=models.CharField(default=7, max_length=20),
            preserve_default=False,
        ),
    ]
