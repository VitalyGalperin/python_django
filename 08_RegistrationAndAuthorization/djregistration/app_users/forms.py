from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    username = forms.CharField(max_length=30, required=False, label='Пользователь')
    email = forms.EmailField(required=False, label='email')
    phone = forms.CharField(max_length=12, required=False, label='Телефон')
    city = forms.CharField(max_length=30, required=False, label='Город')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class AccountForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    username = forms.CharField(max_length=30, required=False, label='Пользователь')
    phone = forms.CharField(max_length=13, required=False, label='Телефон')
    city = forms.CharField(max_length=30, required=False, label='Город')
    is_verified = forms.BooleanField(label='Верифицирован')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )
