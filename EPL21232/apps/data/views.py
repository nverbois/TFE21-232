from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Station,Data,MeanDay,Intensity, MeanWeek, MeanYear
from datetime import timedelta, date, datetime

# Create your views here.

 
def dynamic_lookup_view(request: HttpRequest, my_id) -> HttpResponse:
    # The concerned station 
    station = Station.objects.get(id=my_id)
    # 10 latests data for the station
    data = Data.objects.order_by('-tilting_date').filter(station=station)[:10000][::-1]
    # 10 latests means for the station (counting per day !!!)
    meandaytable = MeanDay.objects.filter(station=station).order_by('-mean_day')[::-1]
    meanweektable = MeanWeek.objects.filter(station=station).order_by('-mean_week')[::-1]
    meanyeartable = MeanYear.objects.filter(station=station).order_by('-mean_year')[::-1]
    intensitytable = Intensity.objects.filter(station=station).order_by('-intensity_day')[::-1]
    intensityData = []
    intensityDuration = []
    meandayData = []
    meandayDate = []
    meanweekData = []
    meanweekDate = []
    meanyearData = []
    meanyearDate = []
    precipitation = []
    precipitationDate = []
    precipitationTime = []
    
    for elem in intensitytable:
        intensityData.append(float(elem.intensity))
        intensityDuration.append(float(elem.duration))

    for elem in meandaytable:
        meandayData.append(float(elem.mean_per_day))
        meandayDate.append(str(elem.mean_day))

    for elem in meanweektable:
        meanweekData.append(float(elem.mean_per_week))
        meanweekDate.append(str(elem.mean_week))

    for elem in meanyeartable:
            meanyearData.append(float(elem.mean_per_year))
            meanyearDate.append(str(elem.mean_year))


    lastday = data[len(data)-1].tilting_date

    for elem in data:
        if elem.tilting_date == lastday:
            precipitationTime.append(elem.tilting_time.strftime("%H:%M:%S"))
            precipitation.append(float(elem.tilting_mm))


    shorterintensityData = intensityData[-11:]
    shorterintensityDuration = intensityDuration[-11:]


    context = {
        'id': my_id,
        "data": data,
        "meandaytable": meandaytable,
        "meanweektable": meanweektable,
        "meanyeartable": meanyeartable,
        "intensitytable": intensitytable,
        "station": station,
        "intensityData": shorterintensityData,
        "intensityDuration":shorterintensityDuration,
        "meandayData": meandayData,
        "meandayDate": meandayDate,
        "meanweekData": meanweekData,
        "meanweekDate": meanweekDate,
        "meanyearData": meanyearData,
        "meanyearDate": meanyearDate,
        "shorterData": precipitation,
        "shorterTime": precipitationTime,
    }
    return render(request, "data-old.html", context)

def data(request: HttpRequest) -> HttpResponse:
    return render(request, "data.html")

def getMeanDayData(request,my_id):
    station = Station.objects.get(id=my_id)
    meandayData = []
    meandaytable = MeanDay.objects.filter(station=station).order_by('-mean_day')[::-1]
    for elem in meandaytable:
        meandayData.append(str(elem.mean_per_day))

    return JsonResponse(meandayData, safe = False)


def getMeanWeekData(request,my_id):
    station = Station.objects.get(id=my_id)
    meanweekData = []
    meanweektable = MeanWeek.objects.filter(station=station).order_by('-mean_week')[::-1]
    for elem in meanweektable:
        meanweekData.append(str(elem.mean_per_week))

    return JsonResponse(meanweekData, safe = False)

def getMeanYearData(request,my_id):
    station = Station.objects.get(id=my_id)
    meanyearData = []
    meanyeartable = MeanYear.objects.filter(station=station).order_by('-mean_year')[::-1]
    for elem in meanyeartable:
        meanyearData.append(str(elem.mean_per_year))

    return JsonResponse(meanyearData, safe = False)


def getMaxDayData(request,my_id):
    station = Station.objects.get(id=my_id)
    maxdayData = []
    maxdaytable = MeanDay.objects.filter(station=station).order_by('-mean_day')[::-1]
    for elem in maxdaytable:
        maxdayData.append(str(elem.max_per_day))

    return JsonResponse(maxdayData, safe = False)


def getMinDayData(request,my_id):
    station = Station.objects.get(id=my_id)
    maxdayData = []
    maxdaytable = MeanDay.objects.filter(station=station).order_by('-mean_day')[::-1]
    for elem in maxdaytable:
        maxdayData.append(str(elem.min_per_day))

    return JsonResponse(maxdayData, safe = False)

def getMaxWeekData(request,my_id):
    station = Station.objects.get(id=my_id)
    maxdayData = []
    maxdaytable = MeanWeek.objects.filter(station=station).order_by('-mean_week')[::-1]
    for elem in maxdaytable:
        maxdayData.append(str(elem.max_per_week))

    return JsonResponse(maxdayData, safe = False)


def getMinWeekData(request,my_id):
    station = Station.objects.get(id=my_id)
    maxdayData = []
    maxdaytable = MeanWeek.objects.filter(station=station).order_by('-mean_week')[::-1]
    for elem in maxdaytable:
        maxdayData.append(str(elem.min_per_week))

    return JsonResponse(maxdayData, safe = False)

def getMaxYearData(request,my_id):
    station = Station.objects.get(id=my_id)
    maxdayData = []
    maxdaytable = MeanYear.objects.filter(station=station).order_by('-mean_year')[::-1]
    for elem in maxdaytable:
        maxdayData.append(str(elem.max_per_year))

    return JsonResponse(maxdayData, safe = False)


def getMinYearData(request,my_id):
    station = Station.objects.get(id=my_id)
    maxdayData = []
    maxdaytable = MeanYear.objects.filter(station=station).order_by('-mean_year')[::-1]
    for elem in maxdaytable:
        maxdayData.append(str(elem.min_per_year))

    return JsonResponse(maxdayData, safe = False)