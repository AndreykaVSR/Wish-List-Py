from django.db import models
from django.forms import ModelForm
from django.urls import reverse

# Create your models here.

class Wish(models.Model):
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.description

  def get_absolute_url(self):
    return reverse('home', kwargs={'pk': self.id})