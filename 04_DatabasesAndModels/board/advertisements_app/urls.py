from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='Список объявлений'),
    path('random', views.random, name='Случайное объявление'),
    path('1', views.page1, name='Случайное объявление'),
]
