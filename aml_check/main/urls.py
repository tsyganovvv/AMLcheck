from django.urls import path, include

from main.views import index, check


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('check', check, name='check'),
]