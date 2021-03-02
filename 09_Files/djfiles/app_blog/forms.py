from django import forms
from django.forms import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from .models import Blog, Images


class EditBlogForm(forms.ModelForm):
    images = forms.ImageField(label='Иллюстации ', required=False,
                              widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'title': forms.Textarea(attrs={'label': 'Название '}),
            'description': forms.TextInput(attrs={'label': 'Запись '}),
        }



