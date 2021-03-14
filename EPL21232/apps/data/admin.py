from django.contrib import admin
from .models import Station, Data, Mean, Intensity
from import_export.admin import ImportExportModelAdmin

class StationAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name']


admin.site.register(Station, StationAdmin)

class DataAdmin(ImportExportModelAdmin):
    readonly_fields = ["get_c"]
    fields = ("tilting_date", "tilting_time", "tilting_number", "tilting_mm","get_c")
    list_display = fields
    #list_display = ("tilting_date", "tilting_time", "tilting_number", "tilting_mm","get_c")

    def get_c(self, Data):
        return  1.000
admin.site.register(Data, DataAdmin)

admin.site.register(Mean)
admin.site.register(Intensity)

