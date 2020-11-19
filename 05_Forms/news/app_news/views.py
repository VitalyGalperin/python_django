
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView

from .forms import EditNews
from .models import NewsItem, Comment


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


class AddNewsView(CreateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'


class EditNewsView(UpdateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'

# Удаление записей
# NewsItem.objects.filter(title='').delete()




