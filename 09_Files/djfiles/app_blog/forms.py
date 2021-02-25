from django import forms
from django.forms import inlineformset_factory

from .models import *


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'title': forms.Textarea(attrs={'label': 'Название '}),
            'description': forms.TextInput(attrs={'label': 'Запись '}),
        }


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True, 'label': 'Иллюстации '}),
        }



