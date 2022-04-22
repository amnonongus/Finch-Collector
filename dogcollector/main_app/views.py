from django.shortcuts import render
from django.http import HttpResponse

class Dog:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Kobe', 'cockapoo', 'goodboi Kobe Bwyant', 9),
  Dog('Noodlez', 'chihuahua', 'His Grace', 4),
  Dog('Bailey', 'cockapoo', 'Bailey Boodle', 7)
]


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})