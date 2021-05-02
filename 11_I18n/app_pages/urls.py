from django.urls import path

from app_pages.views import translation_example, greetings_page, welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('welcome/', welcome, name='welcome'),
    path('example/', translation_example, name='example'),
    path('greetings/', greetings_page, name='greetings_page'),

]
