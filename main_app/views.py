from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from .models import Wish


class WishList(ListView):
  model = Wish

class WishCreate(CreateView):
    # print('Wish created')
    model = Wish
    fields = ['description']
    success_url = '/'

class WishDelete(DeleteView):
  model = Wish
  success_url = '/'

def home(request):
    wishes = Wish.objects.all()
    print(wishes)
    return render(request, 'home.html', {'wishes': wishes})

def wishes_index(request):
    print('Wish index')
    wishes = Wish.objects.all()
    return render(request, 'index.html', { 'wishes': wishes })
