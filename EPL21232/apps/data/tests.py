from datetime import date
from django.forms.fields import DurationField
from django.test import TestCase, Client
from .models import Station, Data, MeanDay, MeanWeek, MeanYear, Intensity
from django.utils import timezone
from django.urls import reverse, resolve
from .forms import CustomImportForm, CustomConfirmImportForm
from .urls import *
from . import views


class ModelTest(TestCase):

    def create_station(self):
        return Station.objects.create(name="name_test", description = "descrpiton_test", longitude = 0.0, latitude = 0.0 )
        

    def test_station_creation(self):
        station_test = self.create_station()
        self.assertTrue(isinstance(station_test, Station))
        self.assertEqual(station_test.__str__(), station_test.name)

    def test_data_creation(self):
        station_test = Station.objects.create(name="station_test",  description = "descrpiton_test", longitude = 0.1, latitude = 0.1 )
        data_test = Data.objects.create(station = station_test, date="2000-01-01", heure = "00:00:00", mesure = 0.0)
        self.assertTrue(isinstance(data_test, Data))
        self.assertEqual(data_test.name, 0.0)

    def test_meanDay_creation(self):
        station_test = Station.objects.create(name="station_mean_day_test", description = "descrpiton_test", longitude = 1.1, latitude = 1.1 )
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:00:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:01:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "00:07:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "01:11:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "10:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "13:43:00", mesure = 4.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "17:01:00", mesure = 5.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "23:59:00", mesure = 6.0)
        meanday_test = MeanDay.objects.create(station = station_test, mean_day = "2001-01-03", mean_per_day = 0.0, max_per_day = 0.0, min_per_day = 0.0)
        self.assertTrue(isinstance(meanday_test, MeanDay))
        MeanDay().calculate_mean_per_day
        for mean in MeanDay.objects.all():
            self.assertTrue(isinstance(mean, MeanDay))
            if(str(mean.mean_day) =="2000-01-02"):
                self.assertEqual(mean.mean_per_day, 2.0)
                
            if(str(mean.mean_day) =="2000-01-03"):
                self.assertEqual(mean.mean_per_day ,0.0)
            if(str(mean.mean_day) =="2000-01-04"):
                self.assertEqual(mean.mean_per_day ,3.5)
            

    def test_meanWeek_creation(self):
        station_test = Station.objects.create(name="station_mean_week_test",  description = "descrpiton_test", longitude = 1.1, latitude = 1.1 )
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:00:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:01:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "00:07:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "01:11:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "10:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "13:43:00", mesure = 4.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "17:01:00", mesure = 5.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "23:59:00", mesure = 6.0)
        Data.objects.create(station = station_test, date="2000-02-01", heure = "00:07:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-02-02", heure = "01:11:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-02-02", heure = "10:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-02-04", heure = "13:43:00", mesure = 4.0)
        Data.objects.create(station = station_test, date="2000-02-04", heure = "17:01:00", mesure = 5.0)
        Data.objects.create(station = station_test, date="2000-02-04", heure = "23:59:00", mesure = 6.0)
        meanweek_test = MeanWeek.objects.create(station = station_test, mean_week = "2001-01-10", mean_per_week = 0.0, max_per_week = 0.0, min_per_week = 0.0)
        self.assertTrue(isinstance(meanweek_test, MeanWeek))
        MeanWeek().calculate_mean_per_week
        for mean in MeanWeek.objects.all():
            self.assertTrue(isinstance(mean, MeanWeek))
            if(str(mean.mean_week) =="2000-01-02"):
                self.assertEqual(mean.mean_per_week, 3.0)
            if(str(mean.mean_week) =="2000-01-30"):
                self.assertEqual(mean.mean_per_week,3.5)
            if(str(mean.mean_week) =="2000-01-10"):
                self.assertEqual(mean.mean_per_week,0.0)

    def test_meanYear_creation(self):
        station_test = Station.objects.create(name="station_mean_year_test", description = "descrpiton_test", longitude = 1.1, latitude = 1.1 )
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:00:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:01:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-03", heure = "00:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "00:07:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "01:11:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "10:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "13:43:00", mesure = 4.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "17:01:00", mesure = 5.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "23:59:00", mesure = 6.0)
        Data.objects.create(station = station_test, date="2001-01-01", heure = "00:07:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2001-02-02", heure = "01:11:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2001-02-02", heure = "10:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2001-02-04", heure = "13:43:00", mesure = 4.0)
        Data.objects.create(station = station_test, date="2001-02-04", heure = "17:01:00", mesure = 5.0)
        Data.objects.create(station = station_test, date="2001-02-04", heure = "23:59:00", mesure = 6.0)
        meanyear_test = MeanYear.objects.create(station = station_test, mean_year = "2002", mean_per_year = 0.0, max_per_year = 0.0, min_per_year = 0.0)
        self.assertTrue(isinstance(meanyear_test, MeanYear))
        MeanYear().calculate_mean_per_year
        for mean in MeanYear.objects.all():
            self.assertTrue(isinstance(mean, MeanYear))
            if(str(mean.mean_year) =="2000"):
                self.assertEqual(mean.mean_per_year, 3.0)
            if(str(mean.mean_year) =="2001"):
                self.assertEqual(mean.mean_per_year ,3.5)
            if(str(mean.mean_year) =="2002"):
                self.assertEqual(mean.mean_per_year ,0.0)
            


    def test_Intensity_creation(self):
        station_test = Station.objects.create(name="station_mean_day_test",  description = "descrpiton_test", longitude = 1.1, latitude = 1.1 )
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:05:00", mesure = 3.6)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "01:03:00", mesure = 3.6)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "04:02:00", mesure = 4.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "00:02:00", mesure = 5.0)
        Data.objects.create(station = station_test, date="2000-01-07", heure = "23:59:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-02-18", heure = "00:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-02-18", heure = "07:07:00", mesure = 3.0)
        intensity_test_5 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 5,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "00:04:00", intensity = 0.0)
        intensity_test_10 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 10,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "00:09:00", intensity = 0.0)
        intensity_test_15= Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 15,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "00:14:00", intensity = 0.0)
        intensity_test_20 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 20,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "00:19:00", intensity = 0.0)
        intensity_test_30 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 30,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "00:29:00", intensity = 0.0)
        intensity_test_40 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 40,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "00:39:00", intensity = 0.0)
        intensity_test_50 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 50,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "00:49:00", intensity = 0.0)
        intensity_test_60 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 60,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "00:59:00", intensity = 0.0)
        intensity_test_90 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 90,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "01:29:00", intensity = 0.0)
        intensity_test_120 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 120,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "01:59:00", intensity = 0.0)
        intensity_test_180 = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 180,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "02:59:00", intensity = 0.0)
        self.assertTrue(isinstance(intensity_test_5, Intensity))
        self.assertTrue(isinstance(intensity_test_10, Intensity))
        self.assertTrue(isinstance(intensity_test_15, Intensity))
        self.assertTrue(isinstance(intensity_test_20, Intensity))
        self.assertTrue(isinstance(intensity_test_30, Intensity))
        self.assertTrue(isinstance(intensity_test_40, Intensity))
        self.assertTrue(isinstance(intensity_test_50, Intensity))
        self.assertTrue(isinstance(intensity_test_60, Intensity))
        self.assertTrue(isinstance(intensity_test_90, Intensity))
        self.assertTrue(isinstance(intensity_test_120, Intensity))
        self.assertTrue(isinstance(intensity_test_180, Intensity))
        Intensity().calculate_intensity
        self.assertEqual(len(Intensity.objects.all()),55) # 55 = nombre de jours * nombre de durées différentes
        for intensity in Intensity.objects.all():
            self.assertTrue(isinstance(intensity, Intensity))
            if(str(intensity.intensity_day) =="2000-01-02") and intensity.duration == 5:
                self.assertEqual(float(intensity.intensity), 48.0)
                self.assertEqual(str(intensity.start_interval),"04:00:00")
                self.assertEqual(str(intensity.end_interval),"04:04:00")
            if(str(intensity.intensity_day) =="2000-01-02") and intensity.duration == 60:
                self.assertEqual(float(intensity.intensity ),4.0)
                self.assertEqual(str(intensity.start_interval),"04:00:00")
                self.assertEqual(str(intensity.end_interval),"04:59:00")
            if(str(intensity.intensity_day) =="2000-01-02") and intensity.duration == 180:
                self.assertEqual(float(intensity.intensity),2.4)
                self.assertEqual(str(intensity.start_interval),"00:00:00")
                self.assertEqual(str(intensity.end_interval),"02:59:00")
            if(str(intensity.intensity_day) =="2000-01-04") and intensity.duration == 50:
                self.assertEqual(float(intensity.intensity),6.0)
                self.assertEqual(str(intensity.start_interval),"00:00:00")
                self.assertEqual(str(intensity.end_interval),"00:49:00")
            if(str(intensity.intensity_day) =="2000-01-04") and intensity.duration == 120:
                self.assertEqual(str(intensity.start_interval),"00:00:00")
                self.assertEqual(str(intensity.end_interval),"01:59:00")
                self.assertEqual(float(intensity.intensity) ,2.5)
            if(str(intensity.intensity_day) =="2000-01-07") and intensity.duration == 40:
                self.assertEqual(float(intensity.intensity),4.5)
                self.assertEqual(str(intensity.start_interval),"23:20:00")
                self.assertEqual(str(intensity.end_interval),"23:59:00")
            if(str(intensity.intensity_day) =="2000-01-07") and intensity.duration == 50:
                self.assertEqual(float(intensity.intensity) ,3.6)
                self.assertEqual(str(intensity.start_interval),"23:10:00")
                self.assertEqual(str(intensity.end_interval),"23:59:00")
            if(str(intensity.intensity_day) =="2000-02-18") and intensity.duration == 10:
                self.assertEqual(float(intensity.intensity),18.0)
                self.assertEqual(str(intensity.start_interval),"00:00:00")
                self.assertEqual(str(intensity.end_interval),"00:09:00")
            if(str(intensity.intensity_day) =="2000-02-18") and intensity.duration == 15:
                self.assertEqual(float(intensity.intensity) ,12.0)
                self.assertEqual(str(intensity.start_interval),"00:00:00")
                self.assertEqual(str(intensity.end_interval),"00:14:00")
            if(str(intensity.intensity_day) =="2000-02-18") and intensity.duration == 60:
                self.assertEqual(float(intensity.intensity), 3.0)
                self.assertEqual(str(intensity.start_interval),"00:00:00")
                self.assertEqual(str(intensity.end_interval),"00:59:00")
            if(str(intensity.intensity_day) =="2001-01-03") and intensity.duration == 5:
                self.assertEqual(float(intensity.intensity) ,0.0)
                self.assertEqual(str(intensity.start_interval),"00:00:00")
                self.assertEqual(str(intensity.end_interval),"00:04:00")
            if(str(intensity.intensity_day) =="2001-01-03") and intensity.duration == 30:
                self.assertEqual(float(intensity.intensity) ,0.0)
                self.assertEqual(str(intensity.start_interval),"00:00:00")
                self.assertEqual(str(intensity.end_interval),"00:29:00")


class ViewTest(TestCase):

    def setUp(self) :
        station_test = Station.objects.create(name="test",  description = "descrpiton_test", longitude = 0.1, latitude = 0.1)
        data_1 = Data.objects.create(station = station_test, date="2000-01-02", heure = "00:00:00", mesure = 1.0)
        data_2 = Data.objects.create(station = station_test, date="2000-01-02", heure = "00:01:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-03", heure = "00:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "00:07:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "01:11:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "10:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "13:43:00", mesure = 4.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "17:01:00", mesure = 5.0)
        Data.objects.create(station = station_test, date="2000-12-31", heure = "23:59:00", mesure = 6.0)
        Data.objects.create(station = station_test, date="2001-01-01", heure = "00:07:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2001-02-02", heure = "01:11:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2001-02-02", heure = "10:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2001-02-04", heure = "13:43:00", mesure = 4.0)
        Data.objects.create(station = station_test, date="2001-02-04", heure = "17:01:00", mesure = 5.0)
        Data.objects.create(station = station_test, date="2001-02-04", heure = "23:59:00", mesure = 6.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:05:00", mesure = 3.6)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "01:03:00", mesure = 3.6)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "04:02:00", mesure = 4.0)
        Data.objects.create(station = station_test, date="2000-01-04", heure = "00:02:00", mesure = 5.0)
        Data.objects.create(station = station_test, date="2000-01-07", heure = "23:59:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-02-18", heure = "00:02:00", mesure = 3.0)
        Data.objects.create(station = station_test, date="2000-02-18", heure = "07:07:00", mesure = 3.0)
        MeanDay().calculate_mean_per_day
        MeanWeek().calculate_mean_per_week
        MeanYear().calculate_mean_per_year
        Intensity().calculate_intensity

    def test_view_data(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    # def test_view_dynamic_lookup(self):
    #     print(views)
    #     path = reverse(views.dynamic_lookup_view, kwargs={'my_id': 7})
    #     response = self.client.get(path)
    #     self.assertEqual(response.status_code, 200)





