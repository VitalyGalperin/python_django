from django.urls import path, include
from .views import *

urlpatterns = [

    path('login/', Login2View.as_view(), name='login'),
    path('logout/', Logout2View.as_view(), name='logout'),
    path('register/', Registration2View.as_view(), name='register'),
    path('account/<int:pk>', AccountView.as_view(), name='account'),
]
