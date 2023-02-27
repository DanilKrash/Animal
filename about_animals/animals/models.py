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


class Comment(models.Model):
    author = models.CharField(max_length=64, verbose_name='автор')
    text = models.TextField(blank=False, verbose_name='текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата')
    img = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='картинка', related_name='comments')

    def __str__(self):
        return self.text[:32]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date', ]
