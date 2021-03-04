from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from .models import Blog, Images
from .forms import EditBlogForm, UploadCSVForm
from _csv import reader


class BlogListView(ListView):
    model = Blog
    template_name = 'app_blog/blog_list.html'
    context_object_name = 'blog'
    queryset = Blog.objects.order_by('-created_at')


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
            try:
                blog_save = Blog(
                    title=row[0],
                    description=row[1],
                )
                blog_save.save()
            except:
                pass
        return HttpResponseRedirect('/')


