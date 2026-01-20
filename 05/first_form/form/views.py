from django.shortcuts import render
from django.http import HttpResponse


def get_form(request):
    if request.method == "GET":
        return render(
            request, "form/form.html"
        )
    else:
        username = request.POST["name"]
        return HttpResponse(
            f"Dziekujemy, {username}"
        )
