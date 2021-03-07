from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Station,Data
# Create your views here.

    
def dynamic_lookup_view(request: HttpRequest, my_id) -> HttpResponse:
    # The concerned station 
    station = Station.objects.get(id=my_id)
    # 10 latests data for the station
    data = Data.objects.order_by('-tilting_date')[:10][::-1]
    
    
    context = {
        'id': my_id,
        "data": data,
        "station": station
    }
    return render(request, "data-old.html", context)

def data(request: HttpRequest) -> HttpResponse:
    return render(request, "data.html")