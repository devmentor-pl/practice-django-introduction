from django.shortcuts import render, HttpResponse
import datetime


def hello(request):
    return HttpResponse('To jest mój pierwszy widok w Django!')


def info(request):
    author = "Anna Nowak"
    year = datetime.datetime.now().year
    return render(request, 'first_app/info.html', {'author': author, 'year': year})


def greet(request, name):
    return HttpResponse(f'Witaj, {name}!')