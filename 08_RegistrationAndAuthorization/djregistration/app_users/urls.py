from django.urls import path, include
from .views import Login2View, Logout2View, register_view, AccountView

urlpatterns = [

    path('login/', Login2View.as_view(), name='login'),
    path('logout/', Logout2View.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('account/', AccountView.as_view(), name='account'),
]
