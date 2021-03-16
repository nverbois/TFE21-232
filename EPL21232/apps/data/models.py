from django.db import models
from django.db.models import Avg, Max, Min, Sum 
from decimal import Decimal

import simplejson as json

from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

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
    tilting_number = models.IntegerField()
    tilting_date= models.DateField()
    tilting_time = models.TimeField()
    # Nous allons utilisés des nombres décimaux à 10 chiffes maximum et une presicion de 3 après la virgule du nombre.
    tilting_mm = models.DecimalField(max_digits=10,decimal_places=3)
    # mm_per_minute = models.DecimalField(max_digits=10,decimal_places=3)
    # mm_per_hour = models.DecimalField(max_digits=10,decimal_places=3)
    # mm_per_day = models.DecimalField(max_digits=10,decimal_places=3)

    class Meta:
        verbose_name = 'Donnée pluviométrique'
        verbose_name_plural = 'Données pluviométriques'

class MeanDay(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    # Date du jour de la moyenne
    #id_day = models.ForeignKey(Data)
    mean_day = models.DateField()
    mean_per_day = mean_per_day = models.DecimalField(max_digits=10,decimal_places=3)
    # def __unicode__(self):             
    #     return self.description

    # @property
    # def tilting_mm(self):
    #     return self.id_day.tilting_mm
    
    class Meta:
        verbose_name = 'Moyenne journalière'
        verbose_name_plural = 'Moyennes journalières'

    @property
    def calculate_mean_per_day(self):
        var1 = Data.objects.order_by('-tilting_date')
        oldest_date = var1.last().tilting_date
        newest_date = var1.first().tilting_date
        station = var1.last().station
        for single_date in daterange(oldest_date, newest_date):
            mpd = json.dumps(Data.objects.filter(tilting_date=single_date).aggregate(Avg('tilting_mm'))['tilting_mm__avg'], use_decimal=True)
            mean_object = MeanDay()
            mean_object.station = station
            mean_object.mean_day = single_date
            mean_object.mean_per_day = mpd
            mean_object.save()
        return mpd

class MeanWeek(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    # Date du jour du début de la semaine de la moyenne
    mean_week = models.DateField()
    mean_per_week = models.DecimalField(max_digits=10,decimal_places=3)

    class Meta:
        verbose_name = 'Moyenne hebdomadaire'
        verbose_name_plural = 'Moyennes hebdomadaires'

class MeanYear(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    # Année de la moyenne
    mean_year = models.IntegerField()
    mean_per_year = models.DecimalField(max_digits=10,decimal_places=3)

    class Meta:
        verbose_name = 'Moyenne annuelle'
        verbose_name_plural = 'Moyennes annuelles'
        

    

class Intensity(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    intensity_day = models.DateField()
    duration = models.TimeField()
    # Nous allons utilisés des nombres décimaux à 10 chiffes maximum et une presicion de 3 après la virgule du nombre.
    max_amount = models.DecimalField(max_digits=10,decimal_places=3)
    start_interval = models.DecimalField(max_digits=10,decimal_places=3)
    end_interval = models.DecimalField(max_digits=10,decimal_places=3)
    intensity = models.DecimalField(max_digits=10,decimal_places=3)

    class Meta:
        verbose_name = 'Intensité pluviométrique'
        verbose_name_plural = 'Intensités pluviométriques'

