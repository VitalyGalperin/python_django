from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .forms import EditNews, AddComment
from .models import NewsItem, Comment


class NewsListView(ListView):
    model = NewsItem
    template_name = 'app_news/newsitem_list.html'
    context_object_name = 'newsitems'

    def get_queryset(self):
        if not self.request.user.has_perm('can_view_unverified'):
            return NewsItem.objects.filter(is_active=True).order_by('-edit_at')
        else:
            return NewsItem.objects.order_by('-edit_at')


class NewsDetailView(DetailView):
    model = NewsItem
    template_name = 'app_news/newsitem_detail.html'
    context_object_name = 'newsitem'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddNewsView(CreateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('add_newsitem'):
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)

    def get_form_class(self):
        if not self.request.user.has_perm('can_publish'):
            self.fields = ['title', 'description']
        else:
            self.fields = ['title', 'description', 'is_active']
        return self.form_class


class EditNewsView(UpdateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('add_newsitem'):
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)

    def get_form_class(self):
        if not self.request.user.has_perm('can_publish'):
            self.fields = ['title', 'description']
        else:
            self.fields = ['title', 'description', 'is_active']
        return self.form_class


class AddNewsComment(CreateView):
    model = Comment
    template_name = 'app_news/add_comment.html'
    form_class = AddComment

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            save_user = self.request.user
            save_user_name = self.request.user.username
        else:
            save_user = None
            save_user_name = None
        save_comment = Comment(user_name=save_user_name,
                               comment=form.cleaned_data['comment'],
                               news_fk_id=self.kwargs['pk'],
                               user=save_user
                               )
        save_comment.save()
        return HttpResponseRedirect(reverse('NewsDetailView', args=[self.kwargs['pk']]))

    # def get_form_class(self):
    #     if self.request.user.is_authenticated:
    #         self.fields = ['comment', ]
    #     else:
    #         self.fields = ['comment', ]
    #     return self.form_class



