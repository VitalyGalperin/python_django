from django.urls import path, include
from .views import login_view, Login2View

urlpatterns = [
    path('login/', login_view, name='login'),
    path('login2/', Login2View.as_view(), name='login2'),
]
