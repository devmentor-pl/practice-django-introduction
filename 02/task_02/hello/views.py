from django.http import HttpResponse


def hello(request):
    return HttpResponse("To mój pierwszy widok w Django!")
