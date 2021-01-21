from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NewsItem


@receiver(post_save, sender=NewsItem)
def post_save_news(sender, instance, created, **kwargs):
    if created:
        NewsItem.objects.create()
