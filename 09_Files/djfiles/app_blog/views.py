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
    form_class = EditBlogForm
    template_name = 'app_blog/edit_blog.html'
    success_url = reverse_lazy('BlogListView')
    # permission_required = 'app_blog.add_blog'

    def get_context_data(self, **kwargs):
        context = super(AddBlogView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['image_form'] = ImagesForm(self.request.POST)
        else:
            context['image_form'] = ImagesForm()
        return super().get_context_data(**context)

    def form_valid(self, form):
        context = self.get_context_data()
        image_form = context['image_form']
        if image_form.is_valid():
            for item in image_form.fields['image']:
                Images.objects.create(image=item)
            return HttpResponseRedirect('app_blog/blog_list.html')
        else:
            return self.render_to_response(self.get_context_data(form=form))


# class EditBlogView(PermissionRequiredMixin, UpdateView):
class EditBlogView(UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'app_blog/edit_blog.html'
    success_url = reverse_lazy('BlogListView')
    permission_required = 'app_blog.edit_blog'

    def get_context_data(self, **kwargs):
        context = super(EditBlogView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['image_form'] = ImagesForm(self.request.POST)
        else:
            context['image_form'] = ImagesForm()
        return super().get_context_data(**context)

    def form_valid(self, form):
        context = self.get_context_data()
        image_form = context['image_form']
        if image_form.is_valid():
            for item in image_form.fields['image']:
                Images.objects.create(image=item)
            return HttpResponseRedirect('app_blog/blog_list.html')
        else:
            return self.render_to_response(self.get_context_data(form=form))