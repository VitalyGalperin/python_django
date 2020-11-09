from random import randint
import datetime
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Advertisement


def main(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()[:3]
    content = {'advertisements': advertisements}
    return render(request, 'advertisements_app/main.html', content)


def random(request, *args, **kwargs):
    count = Advertisement.objects.count()
    random_object = Advertisement.objects.all()[randint(0, count - 1)]
    content = {'advertisements': random_object}
    return render(request, 'advertisements_app/random.html', content)


class AdsListView(ListView):
    model = Advertisement
    template_name = 'advertisements.html'
    context_object_name = 'advertisements'
    queryset = Advertisement.objects.all()[:5]


class AdsDetailView(DetailView):
    model = Advertisement

