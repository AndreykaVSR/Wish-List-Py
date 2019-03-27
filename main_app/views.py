from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Wish

# Create your views here.

# class WishForm(ModelForm):

class WishCreate(CreateView):
    print('Wish created')
    model = Wish
    fields = ['description']
    # success_url = '/wishes/'

    def get(self, redirect):
        form = ModelForm()
        wishes = Wish.objects.all()
        print(wishes)

    # def descriprion(self, request):
    #     form = ModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         text = cleaned_date['description']
    #         form = ModelForm()
    #         return redirect('home: home')

# class WishDelete(DeleteView):
#     model = Wish
#     success_url = '/wishes/'

def home(request):
    return render(request, 'home.html')

def wishes_index(request):
    print('Wish index')
    wishes = Wish.objects.all()
    return render(request, 'index.html', { 'wishes': wishes })

# def wish_create(request):
#     wish = Wish.objects.get(id=wish.id)
#     return render(request, 'index.html', { 'wish': wish })

# def wishes_delete(request, wish_id):
#     wish = Wish.objects.get(id=wish.id)
#     return render(request, 'templates/wish_confirm_delete.html', { 'wish': wish })


