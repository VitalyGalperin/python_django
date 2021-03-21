from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Item


def welcome(request):
    return render(request, 'welcome.html')


def add_tasks(request):
    return render(request, 'index.html')


class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'


# def item_list(request):
#     items = Item.objects.all()
#     context = {'items_list': items}
#     return render(request, 'item_list.html', context=context)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'items'
    success_url = reverse_lazy('ItemListView')