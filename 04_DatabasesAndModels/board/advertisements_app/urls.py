from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='Список объявлений'),
    path('fill_db', views.fill_db, name='Добавить 100 записей в БД'),
    path('random', views.random, name='Случайное объявление'),
    path('advertisements', views.AdsListView.as_view(), name='Список объявлений'),
    path('advertisements/<int:pk>', views.AdsDetailView.as_view(), name='Список объявлений детали'),
]
