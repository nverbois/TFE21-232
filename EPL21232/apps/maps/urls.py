from django.conf.urls import url                                                                                                                              
from . import views

app_name="map"
urlpatterns = [ 
    url(r'', views.default_map, name="map"),
]