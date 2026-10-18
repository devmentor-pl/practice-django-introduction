from django.shortcuts import render
import datetime

def my_view(request):
    
    context = {
        "author": "Anna Nowak",
        "year": datetime.datetime.now().year
    }
    
    return render(
        request, 
        "first_app/info.html",
        context
    )
