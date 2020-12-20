from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

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

    def form_valid(self, form):
        save_comment = Comment(user=form.cleaned_data['user'],
                               comment=form.cleaned_data['comment'],
                               news_fk_id=self.kwargs['pk'])
        save_comment.save()
        return HttpResponseRedirect(reverse('NewsDetailView', args=[self.kwargs['pk']]))


# Удаление записей
# NewsItem.objects.filter(title='').delete()
# Comment.objects.all().delete()

# обратная связь
# news = NewsItem.objects.get(pk=25)
# comment = news.news_link.all()
# comment = news.news_set.all() # по умолчению, без related_name
