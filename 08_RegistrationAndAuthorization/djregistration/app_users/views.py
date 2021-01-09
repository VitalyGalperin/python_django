from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import AuthForm, ExtendedRegisterForm, AccountForm
from .models import Profile
from django.contrib.auth.views import LoginView, LogoutView


class Login2View(LoginView):
    template_name = 'users/login.html'


class Logout2View(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            Profile.objects.create(
                user=user,
                city=city,
                phone=phone,
            )
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class AccountView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        return render(request, 'users/account.html')


def edit_account_view(request):
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AccountForm(instance=request.user)
    return render(request, 'users/edit_account.html', {'form': form})

# _________  Not used. notes ____________
#
#
# @permission_required
# def vacancy_list(request):
#     vacancies =Vacancy.objects.all()
#     return render(request, 'vacancy/edit_account.html', {'vacancy_list': vacancies})
#
#
# def vacancy_list(request):
#     if not request.user.has_perm(app_news.view_news): # <app>.<action>_<object_name>
#         raise PermissionDenied()
#     vacancy =Vacancy.objects.all()
#     return render(request, 'vacancy/edit_account.html', {'vacancy_list': vacancy})
#
#
# def base_register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             raw_password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})



