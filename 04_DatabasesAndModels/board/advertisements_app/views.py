from random import randint

from django.shortcuts import render
from .models import Advertisement


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    content = {'advertisements': advertisements}
    return render(request, 'advertisements_app/advertisements.html', content)


def random(request, *args, **kwargs):
    count = Advertisement.objects.count()
    random_object = Advertisement.objects.all()[randint(0, count - 1)]
    content = {'advertisements': random_object}
    return render(request, 'advertisements_app/random.html', content)


def ads_with_links(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    print(advertisements)
    content = {'advertisements': advertisements}
    return render(request, 'advertisements_app/ads_with_links.html', content)