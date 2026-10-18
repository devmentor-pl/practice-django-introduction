from django.shortcuts import render

def my_view(request, user_name):
    
    context = {"author": user_name}

    return render(
        request, 
        "my_app/greet.html",
        context
    )
