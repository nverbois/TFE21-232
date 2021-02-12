from django.urls import path

from . import views



app_name="public"
urlpatterns = [
    path("", views.index, name="index"),  # root url
    path("about", views.about, name="about"),
    path("data", views.data, name="data"),
]