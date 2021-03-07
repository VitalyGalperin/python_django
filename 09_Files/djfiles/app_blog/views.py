from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from _csv import reader
from datetime import datetime, date

from .models import Blog, Images
from .forms import EditBlogForm, UploadCSVForm


class BlogListView(ListView):
    model = Blog
    template_name = 'app_blog/blog_list.html'
    context_object_name = 'blog'
    queryset = Blog.objects.order_by('-created_at')

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.filter(created_at__lte=datetime.now()).order_by('-created_at')
        return query_set


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'app_blog/blog_detail.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('BlogListView')


class AddBlogView(PermissionRequiredMixin, CreateView):
    form_class = EditBlogForm
    template_name = 'app_blog/add_blog.html'
    success_url = reverse_lazy('BlogListView')
    permission_required = 'app_blog.add_blog'

    def form_valid(self, form):
        save_user = self.request.user
        blog_save = Blog(
            user=save_user,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
        )
        blog_save.save()
        for get_image in self.request.FILES.getlist('images'):
            image_save = Images(
                image=get_image,
                blog=blog_save)
            image_save.save()
        return HttpResponseRedirect('/')


class EditBlogView(PermissionRequiredMixin, UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'app_blog/edit_blog.html'
    success_url = reverse_lazy('BlogListView')
    permission_required = 'app_blog.change_blog'

    def form_valid(self, form):
        blog_save = form.save()
        for get_image in self.request.FILES.getlist('images'):
            image_save = Images(
                image=get_image,
                blog=blog_save)
            image_save.save()
        return HttpResponseRedirect('/')


class UploadCSVView(FormView):
    form_class = UploadCSVForm
    template_name = 'app_blog/Upload_blog.html'
    success_url = reverse_lazy('BlogListView')
    permission_required = 'app_blog.add_blog'

    def form_valid(self, form):
        blog_file = form.cleaned_data['CSV_files'].read()
        blog_file_str = blog_file.decode('utf-8').split('\n')
        csv_reader = reader(blog_file_str, delimiter=';', quotechar='"')
        for row in csv_reader:
            save_date = None
            if len(row) and row[0]:
                save_title = row[0]
            else:
                continue
            if row[1]:
                save_description = row[1]
            else:
                continue
            if row[2]:
                get_date = row[2]
                try:
                    save_date = datetime(day=int(get_date[:2]), month=int(get_date[3:5]), year=int(get_date[6:10]))
                except:
                    messages.add_message(self.request, messages.ERROR, 'Дата не соответствует формату')
            if not save_date or save_date < datetime.now():
                save_date = datetime.now()
            if save_title and save_description and save_date:
                blog_save = Blog(
                    title=save_title,
                    description=row[1],
                    created_at=save_date
                )
                blog_save.save()
        return HttpResponseRedirect('/')


