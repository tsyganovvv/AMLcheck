from django.shortcuts import render
from django.urls import reverse


def index(request):
    context = {
        'user': '1'
    }
    return render(request, 'ton/index.html', context)
