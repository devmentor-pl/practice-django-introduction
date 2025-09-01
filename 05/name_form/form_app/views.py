from django.shortcuts import render
from django.http import HttpResponse


def form_view(request):
    if request.method == 'GET':
        return render(request, 'form_app/form.html')
    else:
        name = request.POST['name']
        return HttpResponse(f'Dziękuję {name}')


# Create your views here.
