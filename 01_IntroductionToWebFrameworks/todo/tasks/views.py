from django.http import HttpResponse

from django.views import View
import random


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(create_response())


def create_response():
    list_items = ['<li>Пункт 1</li>', '<li>Пункт 2</li>', '<li>Пункт 3</li>', '<li>Пункт 4</li>', '<li>Пункт 5</li>']
    random.shuffle(list_items)
    response = '<ul>'
    for item in list_items:
        response += item
    response += '<ul>'
    return response
