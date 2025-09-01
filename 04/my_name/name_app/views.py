from django.shortcuts import render
from django.http import HttpResponse


def greet_user(request, my_name):
    return HttpResponse(f'Witaj, {my_name}')
    # Create your views here.
