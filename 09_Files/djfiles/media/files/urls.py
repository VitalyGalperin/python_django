
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('extra_app.urls')),
    path('files/', include('extra_app.urls')),
]
