from django.test import TestCase

import datetime
from django.utils import timezone
from app_blog.forms import EditBlogForm, UploadCSVForm


class BlogFormsTest(TestCase):

    def test_blog_form_field_label(self):
        form = EditBlogForm()
        self.assertTrue(form.fields['title'].label == 'Название')
        self.assertTrue(form.fields['description'].label == 'Запись')

    def test_CSV_form_field_label(self):
        form = UploadCSVForm()
        self.assertTrue(form.fields['CSV_files'].label == 'Статьи блога в формате CSV ')



