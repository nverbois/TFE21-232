from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoibnZlcmJvaXMiLCJhIjoiY2tsbWtkMmtsMGExMjJ2bXVibGVlZDk4NSJ9.QYbY6bF88czsSosuFRi0Zg'
    return render(request, 'map.html', { 'mapbox_access_token': mapbox_access_token })
    