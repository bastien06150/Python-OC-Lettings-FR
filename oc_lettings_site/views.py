from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def triger_error(request):
    raise Exception("This is an error")
