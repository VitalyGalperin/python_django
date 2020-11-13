from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponseRedirect
from .forms import AddNews, EditNews,  UserFieldsForm, UserForm
from .models import User, NewsItem, Comment


class NewsListView(ListView):
    model = NewsItem
    template_name = 'app_news/newsitem_list.html'
    context_object_name = 'newsitems'
    queryset = NewsItem.objects.order_by('-edit_at')[:5]


class NewsDetailView(DetailView):
    model = NewsItem

    # mc = model.objects.get(pk=1)
    #
    # m = mc.news_link.all()
    # print(m)


class AddNewsView(View):
    def get(self, request):
        news_form = AddNews()
        context = {'news_form': news_form}
        return render(request, 'app_news/add_news.html', context)

    def post(self, request):
        news_form = AddNews(request.POST)
        if news_form.is_valid():
            add_news = NewsItem()
            add_news.title = request.POST.get('title')
            add_news.description = request.POST.get('description')
            add_news.title = request.POST.get('is_active')
            add_news.save()
        return redirect('/')


class EditNewsView(View):
    def get(self, request):
        edit_form = NewsItem.objects.get(id=id)
        # edit_form = EditNews.get()
        context = {'edit_form': edit_form}
        return render(request, 'app_news/edit_news.html', context)

    def post(self, request):
        edit_form = AddNews(request.POST)
        if edit_form.is_valid():
            edit_news = NewsItem()
            edit_news.title = request.POST.get('title')
            edit_news.description = request.POST.get('description')
            edit_news.title = request.POST.get('is_active')
            edit_news.save()
        return redirect('/')

# Удаление записей
# NewsItem.objects.filter(title='').delete()


class UserFormView(View):
    def get(self, request):
        user_form = UserFieldsForm()
        content = {'user_form': user_form}
        return render(request, 'app_news/register.html', content)

    def post(self, request):
        user_form = UserFieldsForm(request.POST)
        content = {'user_form': user_form}

        if user_form.is_valid():
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'app_news/register.html', content)

