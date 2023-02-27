from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal
from .forms import AnimalsForm, CommentForm
from django.urls import reverse

from django.views.generic import DetailView


def list(request):
    context = {'animals': Animal.objects.all()}
    return render(request, 'animals/animal_list.html', context)


def animal_detail_view(request, animal_id):
    detail = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.img = detail
            comment.save()
            form = CommentForm()

    else:
        form = CommentForm()
    comment = detail.comments.all()
    context = {'animal_detail': detail, 'comments': comment, 'forms': form}
    return render(request, 'animals/animal_detail.html', context)


def create(request):
    error = ""
    if request.method == 'POST':
        form = AnimalsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неправильно заполнена форма'

    form = AnimalsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'animals/create.html', data)


def save_img_view(request):
    if request.method == 'POST':
        form = AnimalsForm(data=request.POST, files=request.FILES)
        print(form.fields)
        if form.is_valid():
            form.save()
            return redirect(reverse('animals:img'))  # слева пространство имён, справа  название ссылки
    else:
        form = AnimalsForm()

    context = {'form': form}
    return render(request, 'animals/save_img.html', context)
