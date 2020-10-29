from django.shortcuts import render


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements})


def contacts(request, *args, **kwargs):
    contact_details = ['Phone: +972-50-76-789-75',
                       'email: vitalygl@yandex.ru']
    return render(request, 'advertisements/contacts.html', contact_details)
    # contact_details = {'Phone': '+972-50-76-789-75',
    #                    'email': 'vitalygl@yandex.ru'}
    # return render(request, 'advertisements/contacts.html', contact_details)

def about(request, *args, **kwargs):
    about_dict = {'name': 'Бесплатные объявления', 'description': 'Бесплатные объявления в вашем городе!'}
    return render(request, 'advertisements/about.html', about_dict)


def regions(request, *args, **kwargs):
    regions_list = ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область']
    return render(request, 'advertisements/regions.html', {'regions_list': regions_list})


def categories(request, *args, **kwargs):
    categories_list = ['личные вещи', 'транспорт', 'хобби и отдых']
    return render(request, 'advertisements/categories.html', {'categories_list': categories_list})
