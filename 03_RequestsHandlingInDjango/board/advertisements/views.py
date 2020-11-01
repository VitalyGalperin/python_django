from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import ChoiceForm, AdvertisementForm
from .settings import SERVICE_ADVERTISEMENTS, BICYCLE_ADVERTISEMENTS, HOUSE_ADVERTISEMENTS, REGION_LIST, CATEGORIES_LIST


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
        return context


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = '+972-50-76-789-75'
        context['email'] = 'vitalygl@yandex.ru'
        context['address1'] = 'Московское шоссе 29/132, Нижний Новгород, Нижегородская область, Россия, 603116'
        context['address2'] = 'st. Hativat Golani 3309/16,  Eilat, Israel, 8852600'
        return context


def categories(request, *args, **kwargs):
    return render(request, 'advertisements/categories.html', {'categories_list': CATEGORIES_LIST})


class Regions(View):
    def get(self, request):
        return render(request, 'advertisements/regions.html', {'region_list': REGION_LIST})

    def post(self, request):
        regions_list = ['Регион успешно создан']
        return render(request, 'advertisements/regions.html', {'region_list': regions_list})


class IndexPage(View):
    def get(self, request):
        choice_form = ChoiceForm()
        choice_message = ''
        context = {'choice_form': choice_form, 'choice_message': choice_message}
        return render(request, 'advertisements/index.html', context)

    def post(self, request):
        choice_form = ChoiceForm(request.POST)
        choice_message = ''
        if choice_form.is_valid():
            choice_message = 'Данные успешно выбраны'
        context = {'choice_form': choice_form, 'choice_message': choice_message}
        return render(request, 'advertisements/index.html', context)


class Advertisements(View):
    def get(self, request):
        context = {'service_advertisements': SERVICE_ADVERTISEMENTS,
                   'bicycle_advertisements': BICYCLE_ADVERTISEMENTS,
                   'house_advertisements': HOUSE_ADVERTISEMENTS}
        return render(request, 'advertisements/advertisements.html', context)

    def post(self, request):
        post_form = AdvertisementForm()
        message = ['запрос на создание новой записи успешно выполнен']
        context = {'service_advertisements': SERVICE_ADVERTISEMENTS,
                   'bicycle_advertisements': BICYCLE_ADVERTISEMENTS,
                   'house_advertisements': HOUSE_ADVERTISEMENTS,
                   'message': message,
                   'post_form': post_form}
        return render(request, 'advertisements/advertisements.html', context)
