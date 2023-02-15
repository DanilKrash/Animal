from django.db import models


class Animal(models.Model):
    kind = models.CharField(max_length=32, verbose_name='Вид')
    description = models.CharField(max_length=64, verbose_name='Описание')
    birthday = models.DateField(auto_now=False, null=True, blank=True, verbose_name='День рождения')
    image = models.ImageField(upload_to='media/photos/%Y/%m/%d/', verbose_name='Фото')
    name = models.CharField(max_length=32, verbose_name='Имя')

    def __str__(self):
        return self.kind

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'



