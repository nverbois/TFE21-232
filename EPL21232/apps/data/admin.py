from django.contrib import admin
from .models import Station, Data
from import_export.admin import ImportExportModelAdmin

class StationAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name']


admin.site.register(Station, StationAdmin)

class DataAdmin(ImportExportModelAdmin):
    list_display = ("tilting_date", "tilting_time", "tilting_number", "tilting_mm")
admin.site.register(Data, DataAdmin)


