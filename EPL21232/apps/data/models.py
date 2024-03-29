from django.db import models
from django.db.models import Avg, Max, Min, Sum 
from decimal import Decimal

import simplejson as json

from datetime import timedelta, date, datetime

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + timedelta(n)

def yearrange(start_year, end_year):
    for n in range(int(end_year - start_year)+1):
        yield start_year + n

def weekrange(start_week, end_week):
    for n in range(0,int((end_week - start_week).days)+1,7):
        yield start_week + timedelta(n)

#from django.contrib.gis.db import models
#from django.contrib.postgres.operations import CreateExtension
#from django.db import migrations

# class Migration(migrations.Migration):
#
#    operations = [
#        CreateExtension('postgis'),
#        CreateExtension('postgis_topology'),
#    ]

class Station(models.Model):
    # Default location of a station is Haiti center
    name = models.CharField(max_length=64, unique=True, verbose_name="Nom")
    # normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128, blank=True)
    longitude = models.DecimalField(max_digits=13,decimal_places=8, default=-72.285215)
    latitude = models.DecimalField(max_digits=13,decimal_places=8, default=18.971187)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Station pluviométrique'
        verbose_name_plural = 'Stations pluviométriques'

class Data(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    # A voir avec le canva que nous allons imposé, au pire deux méthodes de récolte
    # recolt_type = models.BooleanField()
    date = models.DateField(verbose_name="Date")
    heure = models.TimeField(verbose_name="Heure")
    # Nous allons utilisés des nombres décimaux à 10 chiffes maximum et une presicion de 3 après la virgule du nombre.
    mesure = models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Mesure (en mm)")
    # valuetest = models.DecimalField(max_digits=10,decimal_places=3, default = 0)

    @property
    def name(self):
        return self.mesure

    class Meta:
        ordering = ['date', 'heure']
        verbose_name = 'Donnée pluviométrique'
        verbose_name_plural = 'Données pluviométriques'
        ordering = ['date', 'heure']
        constraints = [
            models.UniqueConstraint(fields=['station', 'date', 'heure'], name='unique data value')
        ]

    def __str__(self):
        return 'Donnée pour ' + self.station.__str__()



class MeanDay(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    mean_day = models.DateField(verbose_name="Jour")
    mean_per_day =  models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Moyenne journalière [mm]")
    max_per_day = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Maximum journalier [mm]")
    min_per_day = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Minimum journalier [mm]")

    
    class Meta:
        ordering = ['mean_day']
        verbose_name = 'Moyenne journalière'
        verbose_name_plural = 'Moyennes journalières'
        constraints = [
            models.UniqueConstraint(fields=['station', 'mean_day'], name='unique mean for a day')
        ]

    @property
    def calculate_mean_per_day(self):
        for station in Station.objects.all():
            var1 = Data.objects.filter(station=station).order_by('-date')
            if var1.last() is None:
                continue
            oldest_date = var1.last().date
            newest_date = var1.first().date
            #station = var1.last().station
            for single_date in daterange(oldest_date, newest_date):
                var2 = var1.filter(date=single_date)
                var3 = var2.aggregate(Avg('mesure'))['mesure__avg']
                day_max = var2.aggregate(Max('mesure'))['mesure__max']
                day_min = var2.aggregate(Min('mesure'))['mesure__min']
                meanpd = json.dumps(var3, use_decimal=True)
                maxpd = json.dumps(day_max, use_decimal=True)
                minpd = json.dumps(day_min, use_decimal=True)
                #print(meanpd)
                #print(var3)
                #print(maxpd)
                #print(minpd)
                if var3 is None: 
                    #print("skipped")
                    continue

                # Will either create the new mean for that day, or update the mean if it already exists
                mean_object, created = MeanDay.objects.get_or_create(station=station,mean_day=single_date)
                mean_object.mean_per_day = meanpd
                mean_object.max_per_day = maxpd
                mean_object.min_per_day = minpd
                mean_object.save()
        return "ok"

class MeanWeek(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    # Date du jour du début de la semaine de la moyenne
    mean_week = models.DateField(verbose_name="Semaine")
    mean_per_week = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Moyenne hebdomadaire [mm]")
    max_per_week = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Maximum hebdomadaire [mm]")
    min_per_week = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Minimum hebdomadaire [mm]")

    class Meta:
        ordering = ['mean_week']
        verbose_name = 'Moyenne hebdomadaire'
        verbose_name_plural = 'Moyennes hebdomadaires'
        constraints = [
            models.UniqueConstraint(fields=['station', 'mean_week'], name='unique mean for a week')
        ]

    @property
    def calculate_mean_per_week(self):
        for station in Station.objects.all():
            #var1 = MeanDay.objects.filter(station=station).order_by('-mean_day')
            var1 = Data.objects.filter(station=station).order_by('-date')
            if var1.last() is None:
                continue
            oldest_date = var1.last().date
            newest_date = var1.first().date


            for single_week in weekrange(oldest_date,newest_date):

                week_span = [single_week, single_week+timedelta(6)]

                var2 = var1.filter(date__range=week_span)
                #print(var2)
                var3 = var2.aggregate(Avg('mesure'))['mesure__avg']
                week_max = var2.aggregate(Max('mesure'))['mesure__max']
                #print(week_max)
                week_min = var2.aggregate(Min('mesure'))['mesure__min']
                meanpw = json.dumps(var3, use_decimal=True)
                maxpw = json.dumps(week_max, use_decimal=True)
                minpw = json.dumps(week_min, use_decimal=True)
                #print(meanpw)
                #print(var3)
                if var3 is None: 
                    #print("skipped")
                    continue

                # Will either create the new mean for that year, or update the mean if it already exists
                mean_object, created = MeanWeek.objects.get_or_create(station=station,mean_week=single_week)
                mean_object.mean_per_week = meanpw
                mean_object.max_per_week = maxpw
                mean_object.min_per_week = minpw
                mean_object.save()

        return "ok"


class MeanYear(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    # Année de la moyenne
    mean_year = models.IntegerField(verbose_name="Année")
    mean_per_year = models.DecimalField(max_digits=10,decimal_places=6,default=0,verbose_name="Moyenne annuelle [mm]")
    max_per_year = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Maximum annuel [mm]")
    min_per_year = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Minimum annuel [mm]")

    class Meta:
        ordering = ['mean_year']
        verbose_name = 'Moyenne annuelle'
        verbose_name_plural = 'Moyennes annuelles'
        constraints = [
            models.UniqueConstraint(fields=['station', 'mean_year'], name='unique mean for a year')
        ]


        
    @property
    def calculate_mean_per_year(self):
        for station in Station.objects.all():
            var1 = Data.objects.filter(station=station).order_by('-date')
            if var1.last() is None:
                continue
            oldest_date = var1.last().date
            newest_date = var1.first().date
            #print(oldest_date.year)
            #print(station)
            for single_year in yearrange(oldest_date.year,newest_date.year):
                start_year = date(single_year,1,1)
                end_year = date(single_year,12,31)
                var2 = var1.filter(date__range=[start_year, end_year])
                var3 = var2.aggregate(Avg('mesure'))['mesure__avg']
                year_max = var2.aggregate(Max('mesure'))['mesure__max']
                year_min = var2.aggregate(Min('mesure'))['mesure__min']
                meanpy = json.dumps(var3, use_decimal=True)
                maxpy = json.dumps(year_max, use_decimal=True)
                minpy = json.dumps(year_min, use_decimal=True)
                #print(meanpy)
                #print(var3)
                if var3 is None: 
                    #print("skipped")
                    continue
                
                # Will either create the new mean for that year, or update the mean if it already exists
                mean_object, created = MeanYear.objects.get_or_create(station=station,mean_year=single_year)
                #print(mean_object.station)
                mean_object.mean_per_year = meanpy
                mean_object.max_per_year = maxpy
                mean_object.min_per_year = minpy
                #print(meanpy)
                #print(mean_object.mean_per_year)
                mean_object.save()
        return "ok"



class Intensity(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    intensity_day = models.DateField(verbose_name="Jour")
    duration = models.DecimalField(max_digits=10,decimal_places=0,default = 1, verbose_name="Durée [min]")
    # Nous allons utilisés des nombres décimaux à 10 chiffes maximum et une presicion de 3 après la virgule du nombre.
    max_amount = models.DecimalField(max_digits=10,decimal_places=3,default = 0, verbose_name="Maximum mesuré [mm]")
    start_interval = models.TimeField(default='00:00', verbose_name="Début de l'intervalle")
    end_interval = models.TimeField(default='23:59', verbose_name="Fin de l'intervalle")
    intensity = models.DecimalField(max_digits=10,decimal_places=3,default = 0, verbose_name="Valeur d'intensité [mm]")

    class Meta:
        verbose_name = 'Intensité pluviométrique'
        verbose_name_plural = 'Intensités pluviométriques'
        constraints = [
            models.UniqueConstraint(fields=['station','intensity_day','duration'], name='unique duration for a station and for a day')
        ]


    @property
    def calculate_intensity(self):
        #initialisation de variables
        max_mm = 0
        max_start = 0
        max_end = 0

        for station in Station.objects.all():
            var1 = Data.objects.filter(station=station).order_by('-date')
            if var1.last() is None:
                print("test")
                continue

            oldest_date = var1.last().date
            newest_date = var1.first().date
            for single_date in daterange(oldest_date, newest_date):

                print(single_date)
                var2 = var1.filter(date=single_date)
                if var2.last() is None: 
                    print("skipped")
                    continue

                day_max = 0
                min_time = var2.first().heure
                max_time = var2.last().heure
                intensity_value = 0
                max_mm = 0
                sum_mm = 0
                


                
                for actual_duration in [5,10,15,20,30,40,50,60,90,120,180]:


                    var3 = var2.order_by('heure') 

                    day_max = 0
                    min_time = var2.first().heure
                    max_time = var2.last().heure
                    intensity_value = 0

                    max_mm = 0
                    max_start = min_time
                    max_end = max_time

                    sum_mm = 0

                    print(actual_duration)

                    periodStart = datetime(2000, 1, 1, 
                                                hour=0,
                                                minute=0,
                                                second=0)
                    
                    periodEnd = periodStart + timedelta(minutes=(actual_duration-1))

                    while periodStart.day < 2 :

                        if(periodEnd.day == 2):
                            periodEnd = datetime(2000, 1, 1, hour= 23, minute= 59, second=0)
                            periodStart = periodEnd - timedelta(minutes=(actual_duration-1))

                        time_span = [periodStart, periodEnd]

                        var4 = var3.filter(heure__range=time_span)

                        if(len(var4) == 0): 
                            sum_mm == 0

                        else:
                            sum_mm = var4.aggregate(Sum('mesure'))['mesure__sum']
                        
                        

                        #keep the biggest sum calculated
                        if sum_mm > max_mm:
                            max_mm = sum_mm
                            max_start = periodStart
                            max_end = periodEnd

                        periodEnd = periodEnd + timedelta(minutes=(actual_duration))
                        periodStart = periodStart + timedelta(minutes=(actual_duration))



                        
                        
                       

                    
                    
                    day_max = max_mm
                    min_time = max_start
                    max_time = max_end
                    intensity_value = day_max * 60 /actual_duration # quantity max / hour
                    

                    #maxvalue = json.dumps(day_max, use_decimal=True)
                    #intensity_val = json.dumps(intensity_value, use_decimal=True)


                    if day_max is None: 
                        print("skipped")
                        continue

                    # Will either create the new mean for that day, or update the mean if it already exists

                    intensity_object, created = Intensity.objects.get_or_create(station=station,intensity_day =single_date,duration =actual_duration)
                    intensity_object.max_amount = day_max
                    intensity_object.start_interval = min_time
                    intensity_object.end_interval = max_time
                    intensity_object.intensity = intensity_value


                    intensity_object.save()
        return "ok"
    

