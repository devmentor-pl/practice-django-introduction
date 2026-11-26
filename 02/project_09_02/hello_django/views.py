from django.shortcuts import render
from django.http import HttpResponse

def hello_django(request):
	return HttpResponse('To mój pierwszy widok w Django!')

# Create your views here.
