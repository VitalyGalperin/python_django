from django.urls import path, include
from .views import *

urlpatterns = [

    path('', add_tasks, name='add_tasks'),
    path('welcome/', welcome, name='welcome'),
    path('item', ItemListView.as_view(), name='ItemListView'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='ItemDetailView'),
]
