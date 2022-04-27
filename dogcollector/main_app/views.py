from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from .forms import WalkForm

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'


class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age', 'toys']


class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

# ======================================================


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    walk_form = WalkForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'walk_form': walk_form})

def add_walk(request, dog_id):
    form = WalkForm(request.POST)
    if form.is_valid():
        new_walk = form.save(commit=False)
        new_walk.dog.id = dog_id
        new_walk.save()
    return redirect('detail', dog_id=dog_id)