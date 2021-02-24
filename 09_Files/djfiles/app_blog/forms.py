from django import forms
from .models import *


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'images']
        widgets = {
            'title': forms.Textarea(attrs={'label': 'Название '}),
            'description': forms.TextInput(attrs={'label': 'Запись '}),
            'images': forms.ClearableFileInput(attrs={'multiple': True, 'label': 'Иллюстации '}),
        }

