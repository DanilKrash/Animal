# Generated by Django 4.1.6 on 2023-02-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_alter_animal_options_alter_animal_birthday_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Животное', 'verbose_name_plural': 'Животные'},
        ),
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
