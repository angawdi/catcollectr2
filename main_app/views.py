from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat
from .forms import CatForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
	cats = Cat.objects.all()
	form = CatForm()
	return render(request, 'index.html', {'cats': cats, 'form':form})

def show(request, cat_id):
	cat = Cat.objects.get(id=cat_id)
	return render(request, 'show.html', {'cat': cat})

def post_cat(request):
	print("POST CAT REACHED!")
	form = CatForm(request.POST)
	if form.is_valid():
		cat = form.save(commit = False)
		cat.save()
	return HttpResponseRedirect('/')