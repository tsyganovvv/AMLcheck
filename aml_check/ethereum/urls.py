from django.urls import path, include

from ethereum.views import index


app_name = 'ethereum'

urlpatterns = [
    path('', index, name='index'),

]