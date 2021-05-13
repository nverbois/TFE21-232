from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Station,Data,MeanDay,Intensity, MeanWeek, MeanYear
from datetime import timedelta, date, datetime

# Create your views here.

 
def dynamic_lookup_view(request: HttpRequest, my_id) -> HttpResponse:
    # The concerned station 
    station = Station.objects.get(id=my_id)
    # 10 latests data for the station
    data = Data.objects.order_by('-date','-heure').filter(station=station)[:10000][::-1]
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
    precipitation = []
    
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


    lastday = data[len(data)-1].date

    dataDic = {}
    timeCounter = datetime(2000, 1, 1, hour= 0, minute= 0, second=0)
    while(timeCounter.day == 1):
        dataDic[timeCounter.strftime("%H:%M:%S")] = 0
        timeCounter = timeCounter + timedelta(minutes= 1)
                
    for elem in data:
        if elem.date == lastday:
            dataDic[str(elem.heure)] = float(elem.mesure)

    for key in dataDic:
        precipitationTime.append(key)
        precipitation.append(dataDic[key])



    shorterintensityData = intensityData[-11:]
    shorterintensityDuration = intensityDuration[-11:]


    lastDay = [str(lastday)]

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
        "lastDayRegistered": lastDay,
    }

    return render(request, "data.html", context)

def data(request: HttpRequest) -> HttpResponse:
    return render(request, "data.html")


def addDailyData(request,my_id):
    station = Station.objects.get(id=my_id)
    dataTable = Data.objects.order_by('-date').filter(station=station)[::-1]
    
    
    dataDic = {}
    for elem in dataTable:
        if str(elem.date) not in dataDic:
            dataDic[str(elem.date)] = {}
            timeCounter = datetime(2000, 1, 1, hour= 0, minute= 0, second=0)
            while(timeCounter.day == 1):
                dataDic[str(elem.date)][timeCounter.strftime("%H:%M:%S")] = 0
                timeCounter = timeCounter + timedelta(minutes= 1)
                
                

    for elem in dataTable:
        dataDic[str(elem.date)][str(elem.heure)] = str(elem.mesure)

    for dic in dataDic:
        newList = []
        for key in dataDic[dic]:
            newList.append(dataDic[dic][key])
            
        dataDic[dic] = newList

        

    return JsonResponse(dataDic, safe = False)

def getMeanDayData(request,my_id):
    station = Station.objects.get(id=my_id)
    meandayData = []
    meandaytable = MeanDay.objects.filter(station=station).order_by('-mean_day')[::-1]
    
    for elem in meandaytable:
        meandayData.append(str(elem.mean_per_day))

    return JsonResponse(meandayData, safe = False)


def addMeanDayData(request,my_id):
    station = Station.objects.get(id=my_id)
    meandaytable = MeanDay.objects.filter(station=station).order_by('-mean_day')[::-1]
    meandayDic = {}

    for elem in meandaytable:

        meandayDic[str(elem.mean_day)] = str(elem.mean_per_day)
        

    return JsonResponse(meandayDic, safe = False)


def getMeanWeekData(request,my_id):
    station = Station.objects.get(id=my_id)
    meanweekData = []
    meanweektable = MeanWeek.objects.filter(station=station).order_by('-mean_week')[::-1]
    for elem in meanweektable:
        meanweekData.append(str(elem.mean_per_week))

    return JsonResponse(meanweekData, safe = False)


def addMeanWeekData(request,my_id):
    station = Station.objects.get(id=my_id)
    meanweektable = MeanWeek.objects.filter(station=station).order_by('-mean_week')[::-1]
    meanweekDic = {}

    for elem in meanweektable:

        meanweekDic[str(elem.mean_week)] = str(elem.mean_per_week)
        

    return JsonResponse(meanweekDic, safe = False)


def getMeanYearData(request,my_id):
    station = Station.objects.get(id=my_id)
    meanyearData = []
    meanyeartable = MeanYear.objects.filter(station=station).order_by('-mean_year')[::-1]
    for elem in meanyeartable:
        meanyearData.append(str(elem.mean_per_year))

    return JsonResponse(meanyearData, safe = False)

def addMeanYearData(request,my_id):
    station = Station.objects.get(id=my_id)
    meanyeartable = MeanYear.objects.filter(station=station).order_by('-mean_year')[::-1]
    meanyearDic = {}

    for elem in meanyeartable:

        meanyearDic[str(elem.mean_year)] = str(elem.mean_per_year)
        

    return JsonResponse(meanyearDic, safe = False)



def getMaxDayData(request,my_id):
    station = Station.objects.get(id=my_id)
    maxdaytable = MeanDay.objects.filter(station=station).order_by('-mean_day')[::-1]
    maxdayDic = {}

    for elem in maxdaytable:
        maxdayDic[str(elem.mean_day)] = str(elem.max_per_day)
        

    return JsonResponse(maxdayDic, safe = False)


def getMinDayData(request,my_id):
    station = Station.objects.get(id=my_id)
    mindaytable = MeanDay.objects.filter(station=station).order_by('-mean_day')[::-1]
    mindayDic = {}

    for elem in mindaytable:
        mindayDic[str(elem.mean_day)] = str(elem.min_per_day)
        

    return JsonResponse(mindayDic, safe = False)

def getMaxWeekData(request,my_id):
    station = Station.objects.get(id=my_id)
    maxweektable = MeanWeek.objects.filter(station=station).order_by('-mean_week')[::-1]
    maxweekDic = {}

    for elem in maxweektable:
        maxweekDic[str(elem.mean_week)] = str(elem.max_per_week)
        

    return JsonResponse(maxweekDic, safe = False)


def getMinWeekData(request,my_id):
    station = Station.objects.get(id=my_id)
    minweektable = MeanWeek.objects.filter(station=station).order_by('-mean_week')[::-1]
    minweekDic = {}

    for elem in minweektable:
        minweekDic[str(elem.mean_week)] = str(elem.min_per_week)
        

    return JsonResponse(minweekDic, safe = False)

def getMaxYearData(request,my_id):
    station = Station.objects.get(id=my_id)
    maxyeartable = MeanYear.objects.filter(station=station).order_by('-mean_year')[::-1]
    maxyearDic = {}

    for elem in maxyeartable:
        maxyearDic[str(elem.mean_year)] = str(elem.max_per_year)
        

    return JsonResponse(maxyearDic, safe = False)


def getMinYearData(request,my_id):
    station = Station.objects.get(id=my_id)
    minyeartable = MeanYear.objects.filter(station=station).order_by('-mean_year')[::-1]
    minyearDic = {}

    for elem in minyeartable:
        minyearDic[str(elem.mean_year)] = str(elem.min_per_year)
        

    return JsonResponse(minyearDic, safe = False)

def addDailyIntensity(request,my_id):
    station = Station.objects.get(id=my_id)
    intensityTable = Intensity.objects.filter(station=station).order_by('-intensity_day')[::-1]
    intensityDic = {}

    for elem in intensityTable:
        if str(elem.intensity_day) not in intensityDic:
            intensityDic[str(elem.intensity_day)] = {int(elem.duration):str(elem.intensity)}
        else:
            intensityDic[str(elem.intensity_day)][int(elem.duration)] = (str(elem.intensity))
    
    for dic in intensityDic:
        newKeys = sorted(intensityDic[dic])
        newList = []
        for key in newKeys:
            newList.append(intensityDic[dic][key])
        intensityDic[dic] = newList
        
        

    return JsonResponse(intensityDic, safe = False)