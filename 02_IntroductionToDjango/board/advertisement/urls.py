from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisements_list, name='advertisements_list.html'),
    path('ad_1', views.ad_1, name='ad_1.html'),
    path('ad_2', views.ad_2, name='ad_2.html'),
    path('ad_3', views.ad_3, name='ad_3.html'),
    path('ad_4', views.ad_4, name='ad_4.html'),
    path('ad_5', views.ad_5, name='ad_5.html'),
]
