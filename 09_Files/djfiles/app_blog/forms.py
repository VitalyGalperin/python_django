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


# class ImagesForm(forms.ModelForm):
#     class Meta:
#         model = Images
#         fields = ['image', ]
#         widgets = {
#             'image': forms.ClearableFileInput(attrs={'multiple': True, 'label': 'Иллюстации '}),
#         }

# class BaseFormset(BaseInlineFormSet):
#     def add_fields(self, form, index):
#         super(BaseFormset, self).add_fields(form, index)
#         form.nested = AddressFormset(
#             instance=form.instance,
#             data=form.data if form.is_bound else None,
#             files=form.files if form.is_bound else None,
#             prefix='address-%s-%s' % (
#                 form.prefix,
#                 AddressFormset.get_default_prefix()),
#             extra=1)
#
#
# ImagesFormset = inlineformset_factory(Blog, Images, formset=BaseFormset, extra=1)


