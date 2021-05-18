from datetime import date
from django.forms.fields import DurationField
from django.test import TestCase
from .models import Station, Data, MeanDay, MeanWeek, MeanYear, Intensity
from django.utils import timezone
from django.urls import reverse
from .forms import CustomImportForm, CustomConfirmImportForm

class ModelTest(TestCase):

    def create_station(self):
        return Station.objects.create(name="name_test", normalized_name="normalized_name_test", description = "descrpiton_test", longitude = 0.0, latitude = 0.0 )
        

    def test_station_creation(self):
        station_test = self.create_station()
        self.assertTrue(isinstance(station_test, Station))
        self.assertEqual(station_test.__str__(), station_test.name)

    def test_data_creation(self):
        station_test = Station.objects.create(name="station_test", normalized_name="normalized_name_test", description = "descrpiton_test", longitude = 0.1, latitude = 0.1 )
        data_test = Data.objects.create(station = station_test, date="2000-01-01", heure = "00:00:00", mesure = 0.0)
        self.assertTrue(isinstance(data_test, Data))
        self.assertEqual(data_test.name, 0.0)

    def test_meanDay_creation(self):
        station_test = Station.objects.create(name="station_mean_day_test", normalized_name="normalized_name_test", description = "descrpiton_test", longitude = 1.1, latitude = 1.1 )
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:00:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:01:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:02:00", mesure = 3.0)
        meanday_test = MeanDay.objects.create(station = station_test, mean_day = "2001-01-03", mean_per_day = 0.0, max_per_day = 0.0, min_per_day = 0.0)
        self.assertTrue(isinstance(meanday_test, MeanDay))
        MeanDay().calculate_mean_per_day
        print(meanday_test)
        print('len')
        print(len(MeanDay.objects.all()))
        for mean in MeanDay.objects.all():
            self.assertTrue(isinstance(mean, MeanDay))

    def test_meanWeek_creation(self):
        station_test = Station.objects.create(name="station_mean_week_test", normalized_name="normalized_name_test", description = "descrpiton_test", longitude = 1.1, latitude = 1.1 )
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:00:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:01:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:02:00", mesure = 3.0)
        meanweek_test = MeanWeek.objects.create(station = station_test, mean_week = "2001-01-03", mean_per_week = 0.0, max_per_week = 0.0, min_per_week = 0.0)
        self.assertTrue(isinstance(meanweek_test, MeanWeek))
        MeanWeek().calculate_mean_per_week
        for mean in MeanWeek.objects.all():
            self.assertTrue(isinstance(mean, MeanWeek))

    def test_meanYear_creation(self):
        station_test = Station.objects.create(name="station_mean_year_test", normalized_name="normalized_name_test", description = "descrpiton_test", longitude = 1.1, latitude = 1.1 )
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:00:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:01:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:02:00", mesure = 3.0)
        meanyear_test = MeanYear.objects.create(station = station_test, mean_year = "2001", mean_per_year = 0.0, max_per_year = 0.0, min_per_year = 0.0)
        self.assertTrue(isinstance(meanyear_test, MeanYear))
        MeanYear().calculate_mean_per_year
        for mean in MeanYear.objects.all():
            self.assertTrue(isinstance(mean, MeanYear))


    def test_Intensity_creation(self):
        station_test = Station.objects.create(name="station_mean_day_test", normalized_name="normalized_name_test", description = "descrpiton_test", longitude = 1.1, latitude = 1.1 )
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:00:00", mesure = 1.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:01:00", mesure = 2.0)
        Data.objects.create(station = station_test, date="2000-01-02", heure = "00:02:00", mesure = 3.0)
        intensity_test = Intensity.objects.create(station = station_test, intensity_day = "2001-01-03", duration = 5,  max_amount = 0.0, start_interval =  "00:00:00", end_interval =  "00:05:00", intensity = 0.0)
        self.assertTrue(isinstance(intensity_test, Intensity))
        Intensity().calculate_intensity
        for intensity in Intensity.objects.all():
            self.assertTrue(isinstance(intensity, Intensity))


