# from django.test import TestCase
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.contrib.auth.models import User
# from app_blog.models import Blog, Images
#
# small_gif = (
#     b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
#     b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
#     b'\x02\x4c\x01\x00\x3b'
# )
#
#
# class BlogModelsTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         test_user = User.objects.create(username='test_user',
#                                         first_name='user_name',
#                                         last_name='user_last_name')
#         test_blog = Blog.objects.create(title='Test title',
#                                         description='Test description',
#                                         user=test_user)
#         Images.objects.create(blog=test_blog,
#                               image=SimpleUploadedFile(name='test_image.jpg', content=small_gif,
#                                                        content_type='image/jpeg'))
#
#     def test_blog_fields_names(self):
#         test_blog = Blog.objects.get(id=1)
#         title = test_blog._meta.get_field('title').verbose_name
#         description = test_blog._meta.get_field('description').verbose_name
#         created_at = test_blog._meta.get_field('created_at').verbose_name
#         self.assertEquals(title, 'Название')
#         self.assertEquals(description, 'Запись')
#         self.assertEquals(created_at, 'Опубликована')
#
#     def test_title_max_length(self):
#         test_blog = Blog.objects.get(id=1)
#         max_length = test_blog._meta.get_field('title').max_length
#         self.assertEquals(max_length, 150)
#
#     def test_blog_foreign_key(self):
#         test_blog = Blog.objects.get(id=1)
#         self.assertEqual(test_blog.user.username, 'test_user')
#
#     def test_image_foreign_key(self):
#         test_image = Images.objects.get(id=1)
#         self.assertEqual(test_image.blog.title, 'Test title')
#
#     def test_image_image_field(self):
#         test_image = Images.objects.get(id=1)
#         self.assertEqual(test_image.image.read(), small_gif)
#         test_image.image.delete()
