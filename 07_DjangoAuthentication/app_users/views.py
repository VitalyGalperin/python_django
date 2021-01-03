from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from .forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if 8 >= datetime.now().hour >= 22:
                    auth_form.add_error('__all__', 'Запрещен вход в систему с 22: до 8:00')
                else:
                    if user.is_superuser:
                        auth_form.add_error('__all__', 'Администратору вход в приложение запрещен')
                    else:
                        if user.is_active:
                            login(request, user)
                            return HttpResponse('Вы успешно вошли в систему')
                        else:
                            auth_form.add_error('__all__', 'Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка логина/пароля')
    else:
        auth_form = AuthForm()
    context = {
        'form': auth_form,
    }
    return render(request, 'users/login.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponse('Вы вышли из учетной записи')


class Login2View(LoginView):
    template_name = 'users/login.html'


class Logout2View(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'

