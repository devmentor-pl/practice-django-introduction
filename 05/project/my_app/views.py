from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
    
    if request.method == 'GET':
        return render(
            request,
            "my_app/form.html"
        )
    else:
        name = request.POST['name']
        return HttpResponse(
            f"Dziękujemy, {name}!"
        )
    