from django import forms
import datetime
from django.core.exceptions import ValidationError

from .models import NewsItem, Comment


class AddNews(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = '__all__'


class EditNews(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = '__all__'


# Пример формы с дополнительной валидацией
class UserFieldsForm(forms.ModelForm):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField()
    birthday = forms.DateField()

    def clean_birthday(self):
        data = self.changed_data['birthday']
        today = datetime.date.today()
        year_delta = (today - data).days / 365
        if year_delta < 18:
            raise ValidationError('Регистрация только старше 18 лет')
        return data

    def clean(self):
        cleaned_data = super(UserFieldsForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == 'Иван' and last_name == 'Иванов':
            msg = 'Запрещено регистрироваться Ивану Иванову'
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
