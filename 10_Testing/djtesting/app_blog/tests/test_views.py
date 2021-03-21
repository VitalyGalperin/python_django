
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from app_blog.models import Blog, Images

NUMBER_OF_ITEMS = 10


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='test_user',
                                        first_name='user_name',
                                        last_name='user_last_name')
        for item_index in range(NUMBER_OF_ITEMS):
            Blog.objects.create(
                title=f'title{item_index}',
                description=f'description{item_index}',
                user=test_user
            )

    def test_blog_exists_at_desired_location(self):
        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/blog_list.html')

    def test_blog_number(self):
        response = self.client.get(reverse('BlogListView'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context_data['blog']) == NUMBER_OF_ITEMS)

    def test_add_blog_exists_at_desired_location(self):
        response = self.client.get('/edit_blog')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/edit_blog.html')
