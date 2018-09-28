from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Cat:
	def __init__(self, name, breed, description, age):
		self.name = name
		self.breed = breed
		self.description = description
		self.age = age

cats = [
	Cat('Lolo', 'tabby', 'foul little demon', 3),
	Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 4 ),
	Cat('Raven', 'black tripod', '3-legged feline', 4)
]
def index(request):
	return render(request, 'index.html', {'cats': cats})
