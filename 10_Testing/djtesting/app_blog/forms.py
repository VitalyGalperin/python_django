from django import forms
from .models import Blog


class EditBlogForm(forms.ModelForm):
    images = forms.ImageField(label='Иллюстации ', required=False,
                              widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'label': 'Название '}),
            'description': forms.Textarea(attrs={'label': 'Запись '}),
        }


class UploadCSVForm(forms.Form):
    CSV_files = forms.FileField(label='Статьи блога в формате CSV ', widget=forms.ClearableFileInput())

    def clean(self):
        cleaned_data = super(UploadCSVForm, self).clean()
        CSV_files = cleaned_data.get('CSV_files')
        if CSV_files.content_type != 'application/vnd.ms-excel':
            msg = 'Разрешена загрузка только файлов в формате CSV'
            self.add_error('CSV_files', msg)

