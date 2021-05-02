from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

# from django_example.views import MainView

urlpatterns = [
    # path('', MainView.as_view(), name='main'),
    # path('', include('app_pages.urls')),
    # path('app_users/', include('app_users.urls')),
    path('', include('app_blog.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('app_users.urls')),
    path('app_pages/', include('app_pages.urls')),
    path('app_goods/', include('app_goods.urls')),
    path('i18n', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
