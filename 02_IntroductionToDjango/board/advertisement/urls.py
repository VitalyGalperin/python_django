from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisements_list, name='advertisements_list.html'),
    path('ad_1', views.ad_1, name='ad_1.html'),
    path('ad_2', views.ad_2, name='ad_2.html'),
]
