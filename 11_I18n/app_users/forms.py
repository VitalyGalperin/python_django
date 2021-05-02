from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class AvatarRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label=_('First name'))
    last_name = forms.CharField(max_length=30, required=False, label=_('Last name'))
    username = forms.CharField(max_length=30, required=False, label=_('Username'))
    avatar = forms.ImageField(label='Аватар ', required=False, )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'avatar')


class AccountForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False, label=_('First name'))
    last_name = forms.CharField(max_length=30, required=False, label=_('Last name'))
    username = forms.CharField(max_length=30, required=False, label=_('Username'))
    avatar = forms.ImageField(label='Аватар ', required=False, )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'avatar')


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()
