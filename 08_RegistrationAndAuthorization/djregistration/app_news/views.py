from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import *
from .models import *


class NewsListView(ListView):
    model = NewsItem
    template_name = 'app_news/newsitem_list.html'
    context_object_name = 'newsitems'

    def get_queryset(self):
        query_set = super().get_queryset()
        if not self.request.user.has_perm('app_users.can_view_unverified'):
            query_set = query_set.filter(is_active=True).order_by('-edit_at').prefetch_related('tag')
        else:
            query_set = query_set.order_by('-edit_at').prefetch_related('tag')
        if self.request.GET.get('tag_search'):
            query_set = query_set.filter(tag__tag__icontains=self.request.GET.get('tag_search'))
        if self.request.GET.get('date_search'):
            get_date = self.request.GET.get('date_search')
            if len(get_date) == 10 and \
                    get_date[:2].isdigit() and get_date[3:5].isdigit() and get_date[6::].isdigit() and \
                    1 <= int(get_date[:2]) <= 31 and \
                    1 <= int(get_date[3:5]) <= 12 and \
                    2000 <= int(get_date[6::]) <= 2100:
                formatted_date = datetime.date(year=int(get_date[6:]), month=int(get_date[3:5]), day=int(get_date[:2]))
                query_set = query_set.filter(created_at__date=formatted_date)
        return query_set


class NewsDetailView(DetailView):
    model = NewsItem
    template_name = 'app_news/newsitem_detail.html'
    context_object_name = 'newsitem'


class AddNewsView(PermissionRequiredMixin, CreateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'
    permission_required = 'app_news.add_newsitem'

    def form_valid(self, form):
        save_user_id = self.request.user.id
        save_newsitem = NewsItem(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            is_active=form.cleaned_data['is_active'],
            creator_id=save_user_id,
        )
        save_newsitem.save()
        tags = form.cleaned_data['tags_string'].split(' ')
        for save_tag in tags:
            if save_tag != '':
                new_tag, created = Tag.objects.get_or_create(tag=save_tag)
                save_newsitem.tag.add(new_tag)
        return HttpResponseRedirect('/')


class EditNewsView(PermissionRequiredMixin, UpdateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'
    permission_required = 'app_news.change_newsitem'

    def get_form_class(self):
        if not self.request.user.has_perm('app_users.can_publish'):
            self.fields = ['title', 'description', 'tags_string', 'tag']
        else:
            self.fields = ['title', 'description', 'is_active', 'tags_string', 'tag']
        return self.form_class

    def form_valid(self, form):
        save_newsitem = form.save()
        tags = form.cleaned_data['tags_string'].split(' ')
        for save_tag in tags:
            if tags != '':
                new_tag, created = Tag.objects.get_or_create(tag=save_tag)
                save_newsitem.tag.add(new_tag)
        return HttpResponseRedirect('/')


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
