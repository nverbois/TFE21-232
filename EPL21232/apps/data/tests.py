from django.test import TestCase
from .models import Station
from django.utils import timezone
from django.urls import reverse
from .forms import CustomImportForm, CustomConfirmImportForm

class StationTest(TestCase):

    def create_station(self):
        return Station.objects.create(name="name_test", normalized_name="normalized_name_test", description = "descrpiton_test", longitude = 0.0, latitude = 0.0 )


    def test_station_creation(self):
        station_test = self.create_station()
        self.assertTrue(isinstance(station_test, Station))
        self.assertEqual(station_test.__str__(), station_test.name)
