from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Station,Data,MeanDay,Intensity
# Create your views here.

    
def dynamic_lookup_view(request: HttpRequest, my_id) -> HttpResponse:
    # The concerned station 
    station = Station.objects.get(id=my_id)
    # 10 latests data for the station
    data = Data.objects.order_by('-tilting_date').filter(station=station)[:10][::-1]
    # 10 latests means for the station (counting per day !!!)
    meandaytable = MeanDay.objects.order_by('-mean_day')[:10][::-1]
    
    
    context = {
        'id': my_id,
        "data": data,
        "meandaytable": meandaytable,
        "station": station
    }
    return render(request, "data-old.html", context)

def data(request: HttpRequest) -> HttpResponse:
    return render(request, "data.html")