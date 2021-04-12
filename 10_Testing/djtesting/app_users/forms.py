from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class AvatarRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    username = forms.CharField(max_length=30, required=False, label='Пользователь')
    avatar = forms.ImageField(label='Аватар ', required=False, )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'avatar')


class AccountForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    username = forms.CharField(max_length=30, required=False, label='Пользователь')
    avatar = forms.ImageField(label='Аватар ', required=False, )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'avatar')


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()
