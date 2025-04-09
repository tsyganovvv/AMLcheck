from django.urls import path, include

from tron.views import index


app_name = 'tron'

urlpatterns = [
    path('', index, name='index'),

]