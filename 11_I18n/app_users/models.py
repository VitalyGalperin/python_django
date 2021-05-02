from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Username'), related_name='avatar_link')
    avatar = models.ImageField(upload_to='images/', blank=True, verbose_name=_('Avatar'))

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _('User avatar')
        verbose_name_plural = _('User avatars')