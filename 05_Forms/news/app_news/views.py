from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponseRedirect
from .forms import AddNews, UserFieldsForm, UserForm
from .models import User, NewsItem, Comment


class NewsListView(ListView):
    model = NewsItem
    template_name = 'app_news/newsitems.html'
    context_object_name = 'newsitems'
    queryset = NewsItem.objects.all()[:5]


class NewsDetailView(DetailView):
    model = NewsItem

    # mc = model.objects.all()
    # print(mc)
    # m = mc.news_fk.all()
    # m = mc.news_link.all()
    # m = mc.comment_set.all()
    # m = mc.Comment_set.all()
    # print(m)


class AddNewsView(View):
    def get(self, request):
        news_form = AddNews()
        context = {'news_form': news_form}
        return render(request, 'app_news/add_news.html', context)

    def post(self, request):
        news_form = AddNews(request.POST)
        context = {}
        if news_form.is_valid():
            add_news = News()
            add_news.save()
            context = {'message': 'Новость добавалена',
                       'news_form': news_form}
        return render(request, 'app_news/add_news.html', context)


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

