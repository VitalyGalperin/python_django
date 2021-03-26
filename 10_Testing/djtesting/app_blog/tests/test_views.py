import os

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from _csv import reader, writer
from datetime import datetime, timedelta
from djtesting.settings import BASE_DIR
from app_blog.models import Blog, Images

NUMBER_OF_ITEMS = 10


class BlogTest(TestCase):
    def setUp(self):
        create_test_users_and_items()
        create_test_csv_file()

    # def test_blog_exists_at_desired_location(self):
    #     login = self.client.login(username='test_user_with_permissions', password='11111')
    #     response = self.client.get('/blog')
    #     self.assertEqual(str(response.context['user']), 'test_user_with_permissions')
    #     self.assertTemplateUsed(response, 'app_blog/blog_list.html')
    #
    # def test_blog_detail_exists_at_desired_location(self):
    #     login = self.client.login(username='test_user_without_permissions', password='22222')
    #     response = self.client.get('/blog/1')
    #     self.assertEqual(str(response.context['user']), 'test_user_without_permissions')
    #     self.assertTemplateUsed(response, 'app_blog/blog_detail.html')
    #
    # def test_blog_number(self):
    #     response = self.client.get(reverse('BlogListView'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(len(response.context_data['blog']) == NUMBER_OF_ITEMS)
    #
    # def test_add_blog_without_permissions(self):
    #     login = self.client.login(username='test_user_without_permissions', password='22222')
    #     response = self.client.get(reverse('AddBlogView'))
    #     self.assertEqual(response.status_code, 403)
    #
    # def test_add_blog_exists_at_desired_location(self):
    #     login = self.client.login(username='test_user_with_permissions', password='11111')
    #     response = self.client.get('/edit_blog')
    #     self.assertEqual(str(response.context['user']), 'test_user_with_permissions')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'app_blog/add_blog.html')
    #
    # def test_change_blog_without_permissions(self):
    #     login = self.client.login(username='test_user_without_permissions', password='22222')
    #     response = self.client.get('/edit_blog/1')
    #     self.assertEqual(response.status_code, 403)
    #
    # def test_change_blog_exists_at_desired_location(self):
    #     login = self.client.login(username='test_user_with_permissions', password='11111')
    #     response = self.client.get('/edit_blog/1')
    #     self.assertEqual(str(response.context['user']), 'test_user_with_permissions')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'app_blog/edit_blog.html')
    #
    # def test_upload_blog_without_permissions(self):
    #     login = self.client.login(username='test_user_without_permissions', password='22222')
    #     response = self.client.get('/upload_blog')
    #     self.assertEqual(response.status_code, 403)
    #
    # def test_upload_blog_exists_at_desired_location(self):
    #     login = self.client.login(username='test_user_with_permissions', password='11111')
    #     response = self.client.get('/upload_blog')
    #     self.assertEqual(str(response.context['user']), 'test_user_with_permissions')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'app_blog/Upload_blog.html')

    def test_upload_blog_verification_and_write_CSV(self):
        login = self.client.login(username='test_user_with_permissions', password='11111')
        test_file = os.path.join(BASE_DIR, 'app_blog', 'tests', 'test_file.csv')
        with open(test_file, 'r', encoding='utf-8') as open_CSV_file:
            CSV_file_in_memory = open_CSV_file.read()
            CSV_file = reader(CSV_file_in_memory, delimiter=';', quotechar='"')
            response = self.client.post(reverse('UploadCSVView'), {'CSV_file': CSV_file})
        self.assertEqual(response['content-type'], 'application/vnd.ms-excel')
        self.assertRedirects(response, reverse('/'))


def create_test_csv_file():
    test_file = os.path.join(BASE_DIR, 'app_blog', 'tests', 'test_file.csv')
    with open(test_file, mode="w", encoding='utf-8') as csv_test_file:
        csv_writer = writer(csv_test_file, delimiter=';', quotechar='"')
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        csv_writer.writerow(['title 1', 'article text 1', yesterday])
        csv_writer.writerow(['', 'title 2', 'article text 2', tomorrow])
        csv_writer.writerow(['title 3', 'article text 3', tomorrow])


def create_test_users_and_items():
    test_user_with_permissions = User.objects.create_user(username='test_user_with_permissions',
                                                          first_name='test_user_with_permissions',
                                                          last_name='user_last_name',
                                                          password='11111')
    test_user_with_permissions.save()
    test_user_without_permissions = User.objects.create_user(username='test_user_without_permissions',
                                                             first_name='test_user_without_permissions',
                                                             last_name='user_last_name',
                                                             password='22222')
    test_user_without_permissions.save()
    permission_add_blog = Permission.objects.get(name='Can add Блог')
    test_user_with_permissions.user_permissions.add(permission_add_blog)
    permission_change_blog = Permission.objects.get(name='Can change Блог')
    test_user_with_permissions.user_permissions.add(permission_change_blog)

    for item_index in range(NUMBER_OF_ITEMS):
        Blog.objects.create(
            title=f'title{item_index}',
            description=f'description{item_index}',
            user=test_user_with_permissions
        )