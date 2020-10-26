from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def advertisements_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisements_list.html', {})


def advertisement(request, *args, **kwargs):
    return HttpResponse(
        '<h2>Создание сайтов на коленке</h2>'
        '<p>Созание сайтов на коленке заказчика. Выполняется опытными тату-мастерами почти без ошибок<br>'
        'Также можем создать сайт на любой другой части тела в пределах дозволенного.<br>'
        'Мастера Давид и Михаэль из Ашдода.     אשדוד, ישראלת</p>'
        '<p><u>+972-50-76-777-77</u>  !!!  Звоните  !!!</p>'

    )