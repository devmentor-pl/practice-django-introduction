from django.shortcuts import render
from django.http import HttpResponse


def form_view(request):
    if request.method == 'GET':
        return render(request, 'form_app/form.html')
    else:
        name = request.POST.get('name', '').strip()
        if not name:
            return render(request, 'form_app/form.html', {'error': 'Pole name nie może być puste!'})

        
        return render(request, 'form_app/form.html', {'name': name})


# Create your views here.
