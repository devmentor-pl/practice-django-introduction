from django.shortcuts import render
import datetime


def first_view(request):
    context = {
        'author': 'autor',
        'year': datetime.datetime.now().year
    }
    return render(request, 'first_app/info.html', context)

    # Create your views here.
