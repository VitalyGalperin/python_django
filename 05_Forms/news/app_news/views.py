from django.views.generic import View, ListView, DetailView, UpdateView, CreateView

from .forms import EditNews, AddComment
from .models import NewsItem, Comment


class NewsListView(ListView):
    model = NewsItem
    template_name = 'app_news/newsitem_list.html'
    context_object_name = 'newsitems'
    queryset = NewsItem.objects.order_by('-edit_at')[:5]


class NewsDetailView(DetailView):
    model = NewsItem
    template_name = 'app_news/newsitem_detail.html'
    context_object_name = 'newsitem'


class AddNewsView(CreateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'


class EditNewsView(UpdateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    context_object_name = 'comment'
    success_url = '/'


class AddNewsComment(CreateView):
    model = Comment
    template_name = 'app_news/add_comment.html'
    form_class = AddComment
    success_url = '/'

    def get_context_data(self, **kwargs):  # Дополнение данных
        context = super().get_context_data(**kwargs)
        context['news_fk_id'] = Comment.objects.get(pk=self.kwargs['pk'])
        return context

# Удаление записей
# NewsItem.objects.filter(title='').delete()


# обратная связь
# news = NewsItem.objects.get(pk=25)
# comment = news.news_link.all()
# comment = news.news_set.all() # по умолчению, без related_name
