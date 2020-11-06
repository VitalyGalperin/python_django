from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='Список объявлений'),
    path('random', views.random, name='Случайное объявление'),
    path('ads_with_links', views.ads_with_links, name='Случайное объявление'),
]
