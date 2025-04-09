from django.shortcuts import render
from django.urls import reverse


def index(request):
    context = {
        'user': '1'
    }
    return render(request, 'main/index.html', context)


def check(request):
    context = {
        'user': '1'
    }
    return render(request, 'main/check.html', context)