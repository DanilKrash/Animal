from .models import Animal, Comment
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class AnimalsForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['kind', 'name', 'description', 'image', 'birthday']

        widgets = {
            'kind': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вид животного'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя животного'
            }),

            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание животного'
            }),
            'birthday': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'День рождения животного'
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': TextInput(attrs={
                'placeholder': 'Введите ваше имя'
            }),
            'text': Textarea(attrs={
                'placeholder': 'Введите текст'
            })
        }
