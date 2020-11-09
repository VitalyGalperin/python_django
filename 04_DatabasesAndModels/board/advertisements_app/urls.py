from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='Список объявлений'),
    path('random', views.random, name='Случайное объявление'),
    path('advertisements', views.AdsListView.as_view(), name='Список объявлений'),
    path('advertisements/<int:pk>', views.AdsDetailView.as_view(), name='Список объявлений детали'),
]
