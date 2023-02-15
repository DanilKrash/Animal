from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalsForm
from django.views.generic import DetailView


def list(request):
    animals = Animal.objects.all()
    return render(request, 'animals/animal_list.html', {'animals': animals})


class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animals/animal_detail.html'
    context_object_name = 'animal'


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