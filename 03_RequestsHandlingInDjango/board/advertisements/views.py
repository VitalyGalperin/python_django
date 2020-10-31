from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class Regions(View):
    def get(self, request):
        regions_list = ['Нижний Новгород', 'Нижегородская область', 'Москва', 'Московская область']
        return render(request, 'advertisements/regions.html', {'regions_list': regions_list})

    def post(self, request):
        regions_list = ['Регион успешно создан']
        return render(request, 'advertisements/regions.html', {'regions_list': regions_list})


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления в вашем городе'
        context['title'] = 'Бесплатные объявления'
        context['description'] = """
        Бесплатные объявления в вашем городе. Доска частных объявлений Lorem ipsum dolor sit amet, consectetur 
        adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
        non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
        return  context


def about(request, *args, **kwargs):
    about_dict = {'name': 'Бесплатные объявления', 'description': 'Бесплатные объявления в вашем городе!'}
    return render(request, 'advertisements/about.html', about_dict)


def contacts(request, *args, **kwargs):
    contact_details = ['Phone: +972-50-76-789-75',
                       'email: vitalygl@yandex.ru']
    return render(request, 'advertisements/contacts.html', {'contact_details': contact_details})


def categories(request, *args, **kwargs):
    categories_list = ['Услуги', 'Дома на продажу', 'Велосипеды и запчасти']
    return render(request, 'advertisements/categories.html', {'categories_list': categories_list})


def advertisement_list(request, *args, **kwargs):
    service_advertisements = [
        """
        Предлагаю услуги классического массажа и баночного массажа. Помогу снять напряжение в теле, оздоровить спину
        и расслабиться. Общий массаж - длительность 90 минут, возможны и другие варианты. Принимаю в районе беговой на
        дому, но также возможен выезд.
        """,
        """
        Предлагаю услугу электроэпиляции (ТЕРМОЛИЗ), помогающая НАВСЕГДА избавиться от нежелательных волос по всему 
        телу. Стаж- 13 лет непрерывной и насыщенной работы в этой сфере. Есть медицинское образование. Можем с Вами
        ассмотреть и выбрать для Вас самый комфортный вид обезболивания из всех существующих. Иглы( вольфрамовая нить)
        - одноразовые, все СТЕРИЛЬНО!!!Цена указана за один час работы( минималка). Делаю на дому( Вы ко мне или я к Вам).
        """,
        """
        Певец и Диджей в одном лице (без посредников и агентств) на Вашу Свадьбу, Юбилей, Торжество, Корпоративное
         Мероприятие, Новогодний праздник. Огромный выбор музыкального материала, все стили и направления музыки. 
         Живой вокал
        """
    ]

    bicycle_advertisements = [
        'Велосипед детский STELS DOLPHIN. Б/У состояние хорошее, полностью рабочий. Разумный торг возможен.',
        """
        Комплект 24х колёс. 72 спицы. Переднее колесо на покрышке wanda 3.0. Размер по осям 100мм. Заднее колесо с 
        ножным тормозом, на покрышке kenda 3.0/ Размер по осям 120мм
        """,
        """
        Электрический велосипед ECO DRIVE SPORT благодаря электродвигателю мощностью 500W развивает максимальную скорость
        до 40 км/ч. Съемная Li-ion аккумуляторная батарея с напряжением 48V и емкостью 13 Ah позволяет преодолеть 
        расстояние в режиме ассистент (при использовании педалей) до 70-100 км, только на ручке газа до 40-50 км. 
        Крепкая рама велосипеда выдерживает нагрузку до 120 кг. Кроме всего прочего велосипед оборудован дисковыми
        механическими тормозами, задним переключателем - 8 скоростей, передним переключателем - 3 скорости, багажником и
        фронтальной фарой.'
        """
    ]

    house_advertisements = [
        """
        Дом в 2 этажа в новом коттеджном поселке! СКИДКА 700 000 рублей! Стоимость указана с учетом скидки. Удобное
        месторасположение за супермаркетом «Лента» на ул. Родионова (490 метров от ОСТАНОВКИ ул. Родионова). Дом сдан, 
        документы готовы к сделке! Общая площадь 114 кв. Без отделки, стоимость составит 11 490 000 руб.',
        """,
        """
        Продаю сад в СТ "Ясная поляна".Своя питьевая скважина.На участке 2 дома.Один деревянный, другой из пеноблока 
        2-х этажный. В доме холодная, горячая вода, санузел, теплые полы.На первом этаже на полу выложена плитка. 
        Ремонт не требуется.Есть яблони и кустарники, малина. Рядом лес.В перспективе будут проводить газ и можно будет
        прописаться. Торг. Срочно.',
        """,
        """
        Продаётся 1/2 дома и земли. В привлекательном месте Нижнего Новгорода, в непосредственной близости набережной
        Гребного канала в Печёрской Слободе. Первая линия.
                """
    ]

    advertisements = {'service_advertisements': service_advertisements,
                      'bicycle_advertisements': bicycle_advertisements, 'house_advertisements': house_advertisements, }
    return render(request, 'advertisements/advertisement_list.html', advertisements)


