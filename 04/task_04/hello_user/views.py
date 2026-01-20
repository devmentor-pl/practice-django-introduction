from django.shortcuts import render

# Create your views here.


def hello(request, username):
    contex = {
        "username": username
    }

    return render(request, "hello_user/hello.html", contex)
