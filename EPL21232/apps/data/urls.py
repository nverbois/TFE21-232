from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name="data"
urlpatterns = [
    path("", views.data, name="data"),
    path("<int:my_id>", views.dynamic_lookup_view, name="station_data"),
    path("<int:my_id>/getMeanDayData", views.getMeanDayData, name="getMeanDayData"),
    path("<int:my_id>/addMeanDayData", views.addMeanDayData, name="addMeanDayData"),
    path("<int:my_id>/getMeanWeekData", views.getMeanWeekData, name="getMeanWeekData"),
    path("<int:my_id>/getMeanYearData", views.getMeanYearData, name="getMeanYearData"),
    path("<int:my_id>/getMaxDayData", views.getMaxDayData, name="getMaxDayData"),
    path("<int:my_id>/getMinDayData", views.getMinDayData, name="getMinDayData"),
    path("<int:my_id>/getMaxWeekData", views.getMaxWeekData, name="getMaxWeekData"),
    path("<int:my_id>/getMinWeekData", views.getMinWeekData, name="getMinWeekData"),
    path("<int:my_id>/getMaxYearData", views.getMaxYearData, name="getMaxYearData"),
    path("<int:my_id>/getMinYearData", views.getMinYearData, name="getMinYearData"),
]