from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view()),
    path('newsitems', views.NewsListView.as_view(), name='Список новостей'),
    path('newsitems/<int:pk>', views.NewsDetailView.as_view(), name='Новость с комментариями'),
    path('add_news/', views.AddNewsView.as_view(), name='Добавить новость'),
    path('edit_news/<int:id>', views.EditNewsView.as_view(), name='Изменить новость'),
    path('register/', views.UserFormView.as_view()),
]
