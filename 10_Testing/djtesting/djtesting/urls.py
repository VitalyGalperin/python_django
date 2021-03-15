from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_blog.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('app_users.urls')),
    path('files/', include('extra_app.urls')),
    path('tests/', include('app_logic.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)