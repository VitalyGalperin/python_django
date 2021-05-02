from django import forms
from .models import Blog
from django.utils.translation import gettext as _


class EditBlogForm(forms.ModelForm):
    images = forms.ImageField(label=_('Images '), required=False,
                              widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'label': _('Title ')}),
            'description': forms.Textarea(attrs={'label': _('Description ')}),
        }


class UploadCSVForm(forms.Form):
    CSV_files = forms.FileField(label=_('Blog articles in CSV format '), widget=forms.ClearableFileInput())

    def clean(self):
        cleaned_data = super(UploadCSVForm, self).clean()
        CSV_files = cleaned_data.get('CSV_files')
        if CSV_files.content_type != 'application/vnd.ms-excel':
            msg = _('Allowed uploading only files in CSV format')
            self.add_error('CSV_files', msg)

