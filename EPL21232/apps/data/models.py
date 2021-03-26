from django.db import models
from django.db.models import Avg, Max, Min, Sum 
from decimal import Decimal

import simplejson as json

from datetime import timedelta, date

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
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
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
    tilting_date= models.DateField(verbose_name="Date")
    tilting_time = models.TimeField(verbose_name="Heure")
    # Nous allons utilisés des nombres décimaux à 10 chiffes maximum et une presicion de 3 après la virgule du nombre.
    tilting_mm = models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Mesure (en mm)")
    # valuetest = models.DecimalField(max_digits=10,decimal_places=3, default = 0)

    @property
    def name(self):
        return self.tilting_mm

    class Meta:
        verbose_name = 'Donnée pluviométrique'
        verbose_name_plural = 'Données pluviométriques'
        constraints = [
            models.UniqueConstraint(fields=['station', 'tilting_date', 'tilting_time'], name='unique data value')
        ]

    def __str__(self):
        return 'Donnée pour ' + self.station.__str__()



class MeanDay(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    mean_day = models.DateField(verbose_name="Jour")
    mean_per_day =  models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Moyenne journalière")
    max_per_day = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Maximum journalier")
    min_per_day = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Minimum journalier")

    
    class Meta:
        verbose_name = 'Moyenne journalière'
        verbose_name_plural = 'Moyennes journalières'
        constraints = [
            models.UniqueConstraint(fields=['station', 'mean_day'], name='unique mean for a day')
        ]

    @property
    def calculate_mean_per_day(self):
        for station in Station.objects.all():
            var1 = Data.objects.filter(station=station).order_by('-tilting_date')
            if var1.last() is None:
                continue
            oldest_date = var1.last().tilting_date
            newest_date = var1.first().tilting_date
            #station = var1.last().station
            for single_date in daterange(oldest_date, newest_date):
                var2 = var1.filter(tilting_date=single_date)
                var3 = var2.aggregate(Avg('tilting_mm'))['tilting_mm__avg']
                day_max = var2.aggregate(Max('tilting_mm'))['tilting_mm__max']
                day_min = var2.aggregate(Min('tilting_mm'))['tilting_mm__min']
                meanpd = json.dumps(var3, use_decimal=True)
                maxpd = json.dumps(day_max, use_decimal=True)
                minpd = json.dumps(day_min, use_decimal=True)
                print(meanpd)
                print(var3)
                print(maxpd)
                print(minpd)
                if var3 is None: 
                    print("skipped")
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
    mean_week = models.DateField()
    mean_per_week = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Moyenne hebdomadaire")
    max_per_week = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Maximum hebdomadaire")
    min_per_week = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Minimum hebdomadaire")

    class Meta:
        verbose_name = 'Moyenne hebdomadaire'
        verbose_name_plural = 'Moyennes hebdomadaires'
        constraints = [
            models.UniqueConstraint(fields=['station', 'mean_week'], name='unique mean for a week')
        ]

    @property
    def calculate_mean_per_week(self):
        for station in Station.objects.all():
            #var1 = MeanDay.objects.filter(station=station).order_by('-mean_day')
            var1 = Data.objects.filter(station=station).order_by('-tilting_date')
            if var1.last() is None:
                continue
            oldest_date = var1.last().tilting_date
            newest_date = var1.first().tilting_date


            for single_week in weekrange(oldest_date,newest_date):

                week_span = [single_week, single_week+timedelta(6)]

                var2 = var1.filter(tilting_date__range=week_span)
                print(var2)
                var3 = var2.aggregate(Avg('tilting_mm'))['tilting_mm__avg']
                week_max = var2.aggregate(Max('tilting_mm'))['tilting_mm__max']
                print(week_max)
                week_min = var2.aggregate(Min('tilting_mm'))['tilting_mm__min']
                meanpw = json.dumps(var3, use_decimal=True)
                maxpw = json.dumps(week_max, use_decimal=True)
                minpw = json.dumps(week_min, use_decimal=True)
                print(meanpw)
                print(var3)
                if var3 is None: 
                    print("skipped")
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
    mean_year = models.IntegerField()
    mean_per_year = models.DecimalField(max_digits=10,decimal_places=6,default=0,verbose_name="Moyenne annuelle")
    max_per_year = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Maximum annuel")
    min_per_year = models.DecimalField(max_digits=10,decimal_places=6,default = 0,verbose_name="Minimum annuel")

    class Meta:
        verbose_name = 'Moyenne annuelle'
        verbose_name_plural = 'Moyennes annuelles'
        constraints = [
            models.UniqueConstraint(fields=['station', 'mean_year'], name='unique mean for a year')
        ]
        
    @property
    def calculate_mean_per_year(self):
        for station in Station.objects.all():
            var1 = Data.objects.filter(station=station).order_by('-tilting_date')
            if var1.last() is None:
                continue
            oldest_date = var1.last().tilting_date
            newest_date = var1.first().tilting_date
            print(oldest_date.year)
            print(station)
            for single_year in yearrange(oldest_date.year,newest_date.year):
                start_year = date(single_year,1,1)
                end_year = date(single_year,12,31)
                var2 = var1.filter(tilting_date__range=[start_year, end_year])
                var3 = var2.aggregate(Avg('tilting_mm'))['tilting_mm__avg']
                year_max = var2.aggregate(Max('tilting_mm'))['tilting_mm__max']
                year_min = var2.aggregate(Min('tilting_mm'))['tilting_mm__min']
                meanpy = json.dumps(var3, use_decimal=True)
                maxpy = json.dumps(year_max, use_decimal=True)
                minpy = json.dumps(year_min, use_decimal=True)
                print(meanpy)
                print(var3)
                if var3 is None: 
                    print("skipped")
                    continue
                
                # Will either create the new mean for that year, or update the mean if it already exists
                mean_object, created = MeanYear.objects.get_or_create(station=station,mean_year=single_year)
                print(mean_object.station)
                mean_object.mean_per_year = meanpy
                mean_object.max_per_year = maxpy
                mean_object.min_per_year = minpy
                print(meanpy)
                print(mean_object.mean_per_year)
                mean_object.save()
        return "ok"



class Intensity(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    intensity_day = models.DateField()
    duration = models.TimeField()
    # Nous allons utilisés des nombres décimaux à 10 chiffes maximum et une presicion de 3 après la virgule du nombre.
    max_amount = models.DecimalField(max_digits=10,decimal_places=3)
    # start_interval = models.TimeField(verbose_name="Heure")
    # end_interval = models.TimeField(verbose_name="Heure")
    start_interval = models.CharField(max_length=64, unique=True)
    end_interval = models.CharField(max_length=64, unique=True)
    intensity = models.DecimalField(max_digits=10,decimal_places=3)

    class Meta:
        verbose_name = 'Intensité pluviométrique'
        verbose_name_plural = 'Intensités pluviométriques'
        constraints = [
            models.UniqueConstraint(fields=['station','intensity_day','duration'], name='unique duration for a station and for a day')
        ]


    @property
    def calculate_intensity(self):
        for station in Station.objects.all():
            var1 = Data.objects.filter(station=station).order_by('-tilting_date')
            if var1.last() is None:
                continue
            oldest_date = var1.last().tilting_date
            newest_date = var1.first().tilting_date
            #station = var1.last().station
            for single_date in daterange(oldest_date, newest_date):
                var2 = var1.filter(tilting_date=single_date)

                for actual_duration in [1,5,10,15,20,30,40,50,60,90,120,180]:
                    
                    day_max = var2.aggregate(Max('tilting_mm'))['tilting_mm__max']
                    min_time = var2.aggregate(Min('tilting_time'))['tilting_time__min']
                    max_time = var2.aggregate(Max('tilting_time'))['tilting_time__max']
                    intensity_value = var2.aggregate(Max('tilting_mm'))['tilting_mm__max']
                    

                    maxvalue = json.dumps(day_max, use_decimal=True)
                    # first_time = json.dumps(min_time,indent=4, sort_keys=True, default=str)
                    # last_time = json.dumps(max_time,indent=4, sort_keys=True, default=str)
                    first_time = json.dumps(min_time)
                    last_time = json.dumps(max_time)
                    intensity_val = json.dumps(intensity_value, use_decimal=True)


                    if maxvalue is None: 
                        print("skipped")
                        continue

                    # Will either create the new mean for that day, or update the mean if it already exists

                    print("efvydgcbushinzokpzouiybugvygubhinjokplokijuybu")
                    print(max_time)
                    intensity_object, created = Intensity.objects.get_or_create(station=station,intensity_day =single_date,duration =actual_duration)
                    intensity_object.mean_per_day = max_amount
                    intensity_object.start_interval = first_time
                    intensity_object.end_interval = last_time
                    intensity_object.intensity = intensity_val
                    intensity_object.save()
        return "ok"

