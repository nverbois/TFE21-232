from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name="data"
urlpatterns = [
    path("", views.data, name="data"),
    path("<int:my_id>", views.dynamic_lookup_view, name="station_data"),
    #path("meanPerDay/", views.meanPerDay, name='meanPerDay'),
]


