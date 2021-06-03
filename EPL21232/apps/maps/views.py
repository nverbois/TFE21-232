from EPL21232.apps.data.views import data
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from EPL21232.apps.data.models import Station,Data
import json 


# Create your views here.

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section

    #Get all the stations
    stations = Station.objects.all()
    #Append everything to a list that will passed to mapbox



    feature_list = []
    stations_with_datas = []
    for station_elem in stations:
        #data = station_elem.data_set.last()
        data = Data.objects.order_by('-date','-heure').filter(station=station_elem)[:10000][::-1]
        if len(data)>0:
            stations_with_datas.append(station_elem)
            if station_elem != stations.last:
                feature_list.append(
                        {
                        'type': 'Feature',
                        'properties': {
                        'description':
                        f'<strong class="lead">{station_elem.name}</strong><p><a href="/data/{station_elem.id}">Données de la station</a> <p>{station_elem.description}</p> </p>',
                        'icon': 'marker'
                        },
                        'geometry': {
                        'type': 'Point',
                        'coordinates': [station_elem.longitude, station_elem.latitude]
                        }
                        },
                )
            else:
                feature_list.append(
                    {
                    'type': 'Feature',
                    'properties': {
                    'description':
                    f'<strong class="lead">{station_elem.name}</strong><p><a href="/data/{station_elem.id}">Données de la station</a> <p>{station_elem.description}</p> </p>',
                    'icon': 'marker'
                    },
                    'geometry': {
                    'type': 'Point',
                    'coordinates': [station_elem.longitude, station_elem.latitude]
                    }
                    }
                )
    

    print(stations)
    print(stations_with_datas)
    mapbox_access_token = 'pk.eyJ1IjoibnZlcmJvaXMiLCJhIjoiY2tsbWtkMmtsMGExMjJ2bXVibGVlZDk4NSJ9.QYbY6bF88czsSosuFRi0Zg'
    return render(request, 'map.html', { 'mapbox_access_token': mapbox_access_token, 'feature_list':feature_list, 'stations': stations_with_datas })

def isEmpty(request,my_id):
    station = Station.objects.get(id=my_id)
    data = Data.objects.order_by('-date','-heure').filter(station=station)[:10000][::-1]
    if len(data) == 0:
         return JsonResponse(True, safe = False)
    else:
        return JsonResponse(False, safe = False)



    