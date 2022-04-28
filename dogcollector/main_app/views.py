from xml.etree.ElementTree import tostring
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dog, Toy
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
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toy.all().values_list('id'))
    walk_form = WalkForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'walk_form': walk_form, 'toys': toys_dog_doesnt_have})

def add_walk(request, dog_id):
    form = WalkForm(request.POST)
    if form.is_valid():
        new_walk = form.save(commit=False)
        new_walk.dog_id = dog_id
        new_walk.save()
    return redirect('detail', dog_id=dog_id)

def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toy.add(toy_id)
    return redirect('detail', dog_id=dog_id)


class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'