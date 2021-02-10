from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "àpropos.html")


def données(request: HttpRequest) -> HttpResponse:
    return render(request, "données.html")
