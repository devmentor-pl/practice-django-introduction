from django.shortcuts import render
import datetime

# Create your views here.
def info_django(request):
    context = {
        'author': 'Anna Nowak',
        'year': datetime.datetime.now().year,
    }
    return render (
        request,
        'first_app/info.html',
        context
    )