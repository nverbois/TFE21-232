from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Station,Data
# Create your views here.

    
def dynamic_lookup_view(request: HttpRequest, my_id) -> HttpResponse: 
    obj = Data.objects.get(id=my_id)
    context = {
        "objects": obj
    }
    return render(request, "data-old.html",{ 'id': my_id})

def data(request: HttpRequest) -> HttpResponse:
    return render(request, "data.html")