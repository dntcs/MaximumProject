# Generated by Django 5.0.6 on 2024-07-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0005_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='advertisements/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
