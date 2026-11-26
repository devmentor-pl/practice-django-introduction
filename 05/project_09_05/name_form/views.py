from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def name_form(request):
    if request.method == 'GET':
        return render(
            request,
            'name_form/name_form.html'
        )
    else:
        name = request.POST['name']
        return HttpResponse(
            f'Dziękujęmy, {name}!'
        )


