from django.urls import path, include
from .views import login_view, Login2View, logout_view, Logout2View

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('login2/', Login2View.as_view(), name='login2'),
    path('logout2/', Logout2View.as_view(), name='logout2'),
]
