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


def page1(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    content = {'advertisements': advertisements}
    return render(request, 'advertisements_app/1.html', content)