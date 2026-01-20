from django.shortcuts import render
from datetime import datetime


def info(request):
    contex = {
        "author": "Anna Nowak",
        "year": datetime.now().year
    }
    
    return render(request, "first_app/info.html", contex)
