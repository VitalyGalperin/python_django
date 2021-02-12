from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('upload_file/', upload_file, name='upload_file'),
    path('upload_files/', upload_files, name='upload_files'),
    path('upload_price/', upload_price, name='upload_price'),
    path('model_upload_file/', model_upload_file, name='model_upload_file'),
    path('item/', item_list, name='item_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
