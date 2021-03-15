from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_tasks/', add_tasks, name='add_tasks'),
    path('upload_file/', upload_file, name='upload_file'),
    path('upload_files/', upload_files, name='upload_files'),
    path('upload_price/', upload_price, name='upload_price'),
    path('model_upload_file/', model_upload_file, name='model_upload_file'),
    path('item/', item_list, name='item_list'),
]
