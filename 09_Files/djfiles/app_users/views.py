from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


class Login2View(LoginView):
    template_name = 'users/login.html'


class Logout2View(LogoutView):
    next_page = '/'


class Registration2View(FormView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(Registration2View, self).form_valid(form)




