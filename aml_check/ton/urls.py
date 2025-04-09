from django.urls import path, include

from ton.views import index


app_name = 'ton'

urlpatterns = [
    path('', index, name='index'),

]