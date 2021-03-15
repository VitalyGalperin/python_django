from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, UpdateView
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
        user_save = form.save()
        avatar = form.cleaned_data['avatar']
        if avatar:
            UserProfile.objects.create(
                user=user_save,
                avatar=avatar,
            )
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password1']
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(Registration2View, self).form_valid(form)


class AccountView(UpdateView):
    model = User
    form_class = AccountForm
    template_name = 'users/account.html'
    success_url = '/'

    def form_valid(self, form):
        user_save = form.save()
        avatar = form.cleaned_data['avatar']
        if avatar:
            old_avatar = UserProfile.objects.filter(user=user_save)
            old_avatar.delete()
            UserProfile.objects.create(
                user=user_save,
                avatar=avatar,
            )
        return HttpResponseRedirect('/')


def restore_password(request):
    if request.method == 'POST':
        form = RestorePasswordForm()
        if form.is_valid():
            new_password = User.objects.make_random_password()
            user_email = form.cleaned_data['email']
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject='Восстановление пароля',
                message='Test',
                from_email='admin@company.com',
                recipient_list=[form.cleaned_data['email']]
            )
            return HttpResponse('Письмо успешно отправлено')
    form = RestorePasswordForm()
    context = {
        'form': form
    }
    return render(request, 'users/restore_password.html', context=context)


