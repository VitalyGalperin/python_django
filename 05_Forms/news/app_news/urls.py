from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view()),
    path('newsitems', views.NewsListView.as_view(), name='Список новостей'),
    path('newsitems/<int:pk>', views.NewsDetailView.as_view(), name='Новость с комментариями'),
    path('edit_news/', views.AddNewsView.as_view(), name='Добавить новость'),
    path('edit_news/<int:pk>', views.EditNewsView.as_view(), name='Изменить новость'),
    path('newsitems/add_comment', views.AddNewsComment.as_view(), name='Добавить комментарий   '),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
