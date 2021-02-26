from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

    
def data(request: HttpRequest) -> HttpResponse:
    return render(request, "data.html")