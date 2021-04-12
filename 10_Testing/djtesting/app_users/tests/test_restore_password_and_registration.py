from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from app_users.forms import AvatarRegisterForm

USER_EMAIL = 'test@company.com'
OLD_PASSWORD = 'testpassword'
SMALL_GIF = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


class RestorePasswordTest(TestCase):
    def test_restore_password_url_exists(self):
        response = self.client.get('/users/restore_password')
        self.assertEqual(response.status_code, 200)

    def test_restore_password_correct_template(self):
        response = self.client.get(reverse('restore_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/restore_password.html')

    def test_post_restore_password(self):
        user = User.objects.create(username='autotest', email=USER_EMAIL)
        response = self.client.post(reverse('restore_password'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 200)
        from django.core.mail import outbox
        self.assertEqual(len(outbox), 1)
        self.assertIn(USER_EMAIL, outbox[0].to)

    def test_if_rassword_was_changed(self):
        user = User.objects.create(username='autotest', email=USER_EMAIL)
        user.set_password(OLD_PASSWORD)
        user.save()
        old_password_hash = user.password
        response = self.client.post(reverse('restore_password'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 200)
        user.refresh_from_db()
        self.assertNotEqual(old_password_hash, user.password)


class RegistrationTest(TestCase):
    def test_registration_url_exists(self):
        response = self.client.get('/users/register')
        self.assertEqual(response.status_code, 301)

    def test_registration_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_registration_valid_data(self):
        form_data = {'first_name': 'test_first_name', 'last_name': 'test_last_name', 'password1': 'password_741852',
                     'password2': 'password_741852', 'username': 'test_username', 'avatar': SMALL_GIF}
        form = AvatarRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'first_name': None, 'last_name': 'test_last_name', 'password1': 'password_741852',
                     'password2': 'password_741852', 'username': 'test_username', 'avatar': SMALL_GIF}
        form = AvatarRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'first_name': 'test_first_name', 'last_name': 'test_last_name', 'password1': None,
                     'password2': 'password_741852', 'username': 'test_username', 'avatar': SMALL_GIF}
        form = AvatarRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {'first_name': 'test_first_name', 'last_name': 'test_last_name', 'password1': 'password_741852',
                     'password2': None, 'username': 'test_username', 'avatar': SMALL_GIF}
        form = AvatarRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {'first_name': 'test_first_name', 'last_name': 'test_last_name', 'password1': '1',
                     'password2': '1', 'username': 'test_username', 'avatar': SMALL_GIF}
        form = AvatarRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {'first_name': 'test_first_name', 'last_name': 'test_last_name', 'password1': 'password_111111',
                     'password2': 'password_222222', 'username': 'test_username', 'avatar': SMALL_GIF}
        form = AvatarRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())


