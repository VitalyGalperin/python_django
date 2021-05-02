from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

UPLOAD_PATH = 'media/images/%Y%m%d/'


class Blog(models.Model):
    title = models.CharField(max_length=150, default='', verbose_name=_('Title'))
    description = models.TextField(default='', null=True, verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('Created at'))
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE,
                             related_name='creator_link')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def get_absolute_url(self):
        return reverse('/', kwargs={'pk': self.pk})


class Images(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name=_('Image'))
    blog = models.ForeignKey(Blog, default=None, null=True, blank=True, on_delete=models.CASCADE,
                             related_name='image_link')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

