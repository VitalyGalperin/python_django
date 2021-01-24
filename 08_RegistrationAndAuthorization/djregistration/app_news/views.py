from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .forms import *
from .models import *


class NewsListView(ListView):
    model = NewsItem
    template_name = 'app_news/newsitem_list.html'
    context_object_name = 'newsitems'

    def get_queryset(self):
        # Permission.objects.filter(id__gte=41).delete()
        # NewsItem.objects.all().delete()
        query_set = super().get_queryset()
        if not self.request.user.has_perm('app_users.can_view_unverified'):
            return query_set.filter(is_active=True).order_by('-edit_at').prefetch_related('tag')
        else:
            return query_set.order_by('-edit_at').prefetch_related('tag')


class NewsDetailView(DetailView):
    model = NewsItem
    template_name = 'app_news/newsitem_detail.html'
    context_object_name = 'newsitem'


class AddNewsView(CreateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('app_news.add_newsitem'):
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        save_user_id = self.request.user.id
        save_newsitem = NewsItem(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            is_active=form.cleaned_data['is_active'],
            creator_id=save_user_id,
                               )
        save_newsitem.save()
        return HttpResponseRedirect('/')


class EditNewsView(UpdateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('app_news.change_newsitem'):
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)

    def get_form_class(self):
        if not self.request.user.has_perm('app_users.can_publish'):
            self.fields = ['title', 'description']
        else:
            self.fields = ['title', 'description', 'is_active']
        return self.form_class


class AddNewsComment(CreateView):
    model = Comment
    template_name = 'app_news/add_comment.html'
    form_class = EditComment

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


class AddTagView(CreateView):
    model = Tag
    template_name = 'app_news/add_tag.html'
    form_class = EditTag

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('app_news.add_newsitem'):
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        save_tag = Tag(tag=form.cleaned_data['tag'])
        save_tag.save()
        return HttpResponseRedirect(reverse('EditNewsView', args=[self.kwargs['pk']]))
