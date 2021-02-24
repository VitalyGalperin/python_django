from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *


class BlogListView(ListView):
    model = Blog
    template_name = 'app_blog/blog_list.html'
    context_object_name = 'blog'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'app_blog/blog_detail.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('BlogListView')


# class AddBlogView(PermissionRequiredMixin, CreateView):
class AddBlogView(CreateView):
    model = Blog
    form_class = EditBlogForm()
    template_name = 'app_blog/edit_blog.html'
    success_url = reverse_lazy('BlogListView')
    # permission_required = 'app_blog.add_blog'

    def form_valid(self, form):
        # blog_item = form.save()
        for item in self.request.FILES.getlist('images'):
            Images.objects.create(image=item)


# class EditBlogView(PermissionRequiredMixin, UpdateView):
class EditBlogView(UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'app_blog/edit_blog.html'
    success_url = reverse_lazy('BlogListView')

