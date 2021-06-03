from django.conf.urls import url                                                                                                                           
from . import views

app_name="map"
urlpatterns = [ 
    url("", views.default_map, name="map"),
    url("<int:my_id>/isEmpty", views.isEmpty, name="isEmpty"),
]