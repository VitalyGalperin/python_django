from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NewsItem
from app_users.models import Profile


@receiver(post_save, sender=NewsItem)
def post_save_news(sender, instance, created, **kwargs):
    if created:
        a = Profile.objects.get(user=instance.creator)
        a.news_number += 1
        a.save()
