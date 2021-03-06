from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('wishes', views.wishes_index, name='index'),
  path('wishes/create/', views.WishCreate.as_view(), name='wishes_create'),
  path('wishes/<int:pk>/delete', views.WishDelete.as_view(), name='wishes_delete')
  # path('wishes/<int:pk>/delete', views.wish_delete, name='wish_delete')
]