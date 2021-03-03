from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from EPL21232.apps.data.models import Station
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
    for station_elem in stations:
        if station_elem != stations.last:
            feature_list.append(
                    {
                    'type': 'Feature',
                    'properties': {
                    'description':
                    f'<strong>{station_elem.name}</strong><p><a href="/data">Données de la station</a> <p>{station_elem.description}</p> </p>',
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
                    '<strong>station_elemn.name</strong><p><a href="/data">Données de la station</a> <p>station_elem.description</p> </p>',
                    'icon': 'marker'
                    },
                    'geometry': {
                    'type': 'Point',
                    'coordinates': [station_elem.longitude, station_elem.latitude]
                    }
                    }
            )


    mapbox_access_token = 'pk.eyJ1IjoibnZlcmJvaXMiLCJhIjoiY2tsbWtkMmtsMGExMjJ2bXVibGVlZDk4NSJ9.QYbY6bF88czsSosuFRi0Zg'
    return render(request, 'map.html', { 'mapbox_access_token': mapbox_access_token, 'feature_list':feature_list })



    