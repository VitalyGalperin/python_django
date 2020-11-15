from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, UpdateView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import AddNews, EditNews,  UserFieldsForm
from .models import User, NewsItem, Comment


class NewsListView(ListView):
    model = NewsItem
    template_name = 'app_news/newsitem_list.html'
    context_object_name = 'newsitems'
    queryset = NewsItem.objects.order_by('-edit_at')[:5]


class NewsDetailView(DetailView):
    model = NewsItem
    template_name = 'app_news/newsitem_detail.html'
    context_object_name = 'newsitems'

    # a = Comment.objects.filter(news_fk_id=id)
    # print(a)


class AddNewsView(View):
    def get(self, request):
        news_form = EditNews
        context = {'news_form': news_form}
        return render(request, 'app_news/edit_news.html', context)

    def post(self, request):
        news_form = EditNews(request.POST)
        if news_form.is_valid():
            news_form.save()
        return redirect('/')


class EditNewsView(UpdateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews

    context_object_name = 'news_form'


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

