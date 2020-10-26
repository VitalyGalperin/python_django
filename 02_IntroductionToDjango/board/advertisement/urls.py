from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisements_list, name='advertisements_list'),
    path('advertisement', views.advertisement, name='advertisement')
]
