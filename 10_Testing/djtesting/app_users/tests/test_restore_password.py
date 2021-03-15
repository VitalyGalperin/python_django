from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

USER_EMAIL = 'user@company.com'
OLD_PASSWORD = 'testpassword'


class RestorePasswordTest(TestCase):
    def test_restore_password_url_exists(self):
        response = self.client.get('/app_users/restore_password/')
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
        self.assertEqual(outbox, 1)
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
