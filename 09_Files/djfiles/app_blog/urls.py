from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view()),
    path('blog', views.BlogListView.as_view(), name='BlogListView'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='BlogDetailView'),
    path('edit_blog', views.AddBlogView.as_view(), name='AddBlogView'),
    path('edit_blog/<int:pk>', views.EditBlogView.as_view(), name='EditBlogView'),
]
