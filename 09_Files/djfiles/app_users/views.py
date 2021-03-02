from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from .models import UserProfile
from .forms import *


class Login2View(LoginView):
    template_name = 'users/login.html'


class Logout2View(LogoutView):
    next_page = '/'


class Registration2View(FormView):
    form_class = AvatarRegisterForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        avatar = form.cleaned_data['avatar']
        UserProfile.objects.create(
            user=user,
            avatar=avatar,
        )
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password1']
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(Registration2View, self).form_valid(form)

    def form_invalid(self, form):
        pass


class AccountView(FormView):
    model = User
    form_class = AvatarRegisterForm
    template_name = 'users/account.html'
    success_url = '/'

    # def get_context_data(self, **kwargs):
    #     context = super(AccountView, self).get_context_data(**kwargs)
    #     context['form'].fields['username'] = self.request.user.username
    #     context['username'] = self.request.user.username
    #     context['first_name'] = self.request.user.first_name
    #     context['last_name'] = self.request.user.last_name
    #     return super().get_context_data(**context)

    def form_valid(self, form):
        user = form.save()
        avatar = form.cleaned_data['avatar']
        UserProfile.objects.create(
            user=user,
            avatar=avatar,
        )
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password1']
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(AccountView, self).form_valid(form)

    def form_invalid(self, form):
        pass
